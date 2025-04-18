def python_versions
def python_executables_and_wheels_map

pipeline {
    agent {
        node {
            label 'zOS_pyRACF'
        }
    }

    parameters {
        // Note: Each Python version listed must be installed on the 
        // build agent and must be added to '$PATH' and '$LIBPATH'.
        string (
            name: "pythonVersions",
            defaultValue: "",
            description: "(Required Always) Comma separated list of Python versions to build wheels for (i.e., Use '10,11' for Python 3.10 and Python 3.11)."
        )
        booleanParam(
            name: "createRelease",
            defaultValue: false,
            description: "Toggle whether or not to create a release from this revision."
        )
        string(
            name: "releaseTag",
            defaultValue: "",
            description: "(Required When Creating Releases) This will be the git tag and version number of the release."
        )
        string(
            name: "gitHubMilestoneLink",
            defaultValue: "",
            description: "(Required When Creating Releases) This is the GitHub Milestore URL that coresponds to the release."
        )
        booleanParam(
            name: "preRelease",
            defaultValue: true,
            description: "Toggle whether or not this is a pre-release."
        )
    }

    options {
        ansiColor('css')
    }

    stages {
        stage('Parameter Validation') {
            steps {
                script {
                    if (params.pythonVersions == "") {
                        error("'pythonVersions' is required parameter.")
                    }
                    if (params.createRelease) {
                        if (params.releaseTag == "") {
                            error("'releaseTag' is a required parameter when creating a release.")
                        }
                        if (params.gitHubMilestoneLink == "") {
                            error("'gitHubMilestoneLink' is a required parameter when creating a release.")
                        }
                    }
                }
            }
        }
        stage('Build Python Executables & Wheels Map') {
            steps {
                script {
                    python_versions = params.pythonVersions.split(",")
                    python_executables_and_wheels_map = (
                        create_python_executables_and_wheels_map(python_versions)
                    )
                }
            }
        }
        stage('Build Virtual Environments') {
            steps {
                script {
                    for (python in python_executables_and_wheels_map.keySet()) {
                        build_virtual_environment(python)
                    }
                }
            }
        }
        stage('Lint & Unit Test') {
            steps {
                script {
                    for (python in python_executables_and_wheels_map.keySet()) {
                        lint_and_unit_test(python)
                    }
                }
            }
        }
        stage('Function Test') {
            steps {
                script {
                    for (python in python_executables_and_wheels_map.keySet()) {
                        function_test(
                            python, 
                            python_executables_and_wheels_map[python]["defaultName"]
                        )
                    }
                }
            }
        }
        stage('Publish') {
            when { 
                expression { params.createRelease == true }    
            }
            steps {
                publish(
                    python_executables_and_wheels_map,
                    params.releaseTag, 
                    env.BRANCH_NAME, 
                    params.gitHubMilestoneLink,
                    params.preRelease
                )
            }
        }
    }
    post {
        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
    }
}

def create_python_executables_and_wheels_map(python_versions) {
    def os = sh(
        returnStdout: true, 
        script: "uname"
    ).trim().replace("/", "").toLowerCase()
    def zos_release = sh(
        returnStdout: true, 
        script: "uname -r"
    ).trim().replace(".", "_")
    def processor = sh(
        returnStdout: true, 
        script: "uname -m"
    ).trim()
    def pyracf_version = sh(
        returnStdout: true, 
        script: "cat pyproject.toml | grep version | cut -d'=' -f2 | cut -d'\"' -f2"
    ).trim()

    python_executables_and_wheels_map = [:]

    for (version in python_versions) {
        python_executables_and_wheels_map["python3.${version}"] = [
            "defaultName": (
                "pyracf-${pyracf_version}-cp3${version}-cp3${version}-${os}_${zos_release}_${processor}.whl"
            ),
            "publishName": "pyracf-${pyracf_version}-cp3${version}-none-any.whl"
        ]
    }

    return python_executables_and_wheels_map
}

def build_virtual_environment(python) {
    echo "Building virtual environment for '${python}'..."

    sh """
        ${python} --version
        rm -rf venv_${python}
        ${python} -m venv venv_${python}
        . venv_${python}/bin/activate
        ${python} -m pip install -r requirements.txt
        ${python} -m pip install -r requirements-development.txt
    """
}

def lint_and_unit_test(python) {
    echo "Running linters and unit tests for '${python}'..."

    sh """
        . venv_${python}/bin/activate
        ${python} -m flake8 .
        ${python} -m pylint --recursive=y .
        cd tests
        ${python} -m coverage run test_runner.py
        ${python} -m coverage report -m
    """
}

def function_test(python, wheel) {
    echo "Running function test for '${python}'..."

    sh """
        git clean -f -d -e 'venv_*'
        . venv_${python}/bin/activate
        ${python} -m pip wheel .
        ${python} -m pip install ${wheel}
        cd tests/function_test
        ${python} function_test.py
    """
}

def publish(
        python_executables_and_wheels_map, 
        release, 
        git_branch, 
        milestone, 
        pre_release
) {
    if (pre_release == true) {
        pre_release = "true"
    }
    else {
        pre_release = "false"
    }
    withCredentials(
        [
            string(
                credentialsId: 'pyracf-github-access-token',
                variable: 'github_access_token'
            )
        ]
    ) {

        // Creating GitHub releases: 
        // https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#create-a-release
        // Uploading release assets: 
        // https://docs.github.com/en/rest/releases/assets?apiVersion=2022-11-28#upload-a-release-asset

        // Use single quotes for credentials since it is the most secure
        // method for interpolating secrets according to the Jenkins docs:
        // https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#string-interpolation

        echo "Creating '${release}' GitHub release..."

        def description = build_description(python_executables_and_wheels_map, release, milestone)

        def release_id = sh(
            returnStdout: true,
            script: (
                'curl -f -v -L '
                + '-X POST '
                + '-H "Accept: application/vnd.github+json" '
                + '-H "Authorization: Bearer ${github_access_token}" '
                + '-H "X-GitHub-Api-Version: 2022-11-28" '
                + "https://api.github.com/repos/ambitus/pyracf/releases "
                + "-d '{"
                + "     \"tag_name\": \"${release}\","
                + "     \"target_commitish\": \"${git_branch}\","
                + "     \"name\": \"${release}\","
                + "     \"body\": \"${description}\","
                + "     \"draft\": false,"
                + "     \"prerelease\": ${pre_release},"
                + "     \"generate_release_notes\":false"
                + "}' | grep '\"id\": ' | head -n1 | cut -d':' -f2 | cut -d',' -f1"
            )
        ).trim()

        for (python in python_executables_and_wheels_map.keySet()) {
            def wheel_default = python_executables_and_wheels_map[python]["defaultName"]
            def wheel_publish = python_executables_and_wheels_map[python]["publishName"]

            echo "Cleaning repo and building '${wheel_default}'..."

            sh """
                git clean -f -d -e 'venv_*'
                . venv_${python}/bin/activate
                ${python} -m pip wheel .
            """

            echo "Uploading '${wheel_default}' as '${wheel_publish}' to '${release}' GitHub release..."

            sh(
                'curl -f -v -L '
                + '-X POST '
                + '-H "Accept: application/vnd.github+json" '
                + '-H "Authorization: Bearer ${github_access_token}" '
                + '-H "X-GitHub-Api-Version: 2022-11-28" '
                + '-H "Content-Type: application/octet-stream" '
                + "\"https://uploads.github.com/repos/ambitus/pyracf/releases/${release_id}/assets?name=${wheel_publish}\" "
                + "--data-binary \"@${wheel_default}\""
            )
        }
    }
}

def build_description(python_executables_and_wheels_map, release, milestone) {
    def description = "Release Milestone: ${milestone}\\n&nbsp;\\n&nbsp;\\n"

    for (python in python_executables_and_wheels_map.keySet()) {
        def wheel = python_executables_and_wheels_map[python]["publishName"]
        def python_executable = python
        def python_label = python.replace("python", "Python ")
        description += (
            "Install for ${python_label}:\\n"
            + "```\\ncurl -O -L https://github.com/ambitus/pyracf/releases/download/${release}/${wheel} "
            + "&& ${python_executable} -m pip install ${wheel}\\n```\\n"
        )
    }

    return description
}
