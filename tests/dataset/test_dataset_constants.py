"""
Sample data for testing Dataset Profile Administration functions.
"""

from typing import Union

import tests.test_utilities as TestUtilities


def get_sample(sample_file: str) -> Union[str, bytes]:
    return TestUtilities.get_sample(sample_file, "dataset")


# ============================================================================
# Dataset Administration Result Sample Data
# ============================================================================

# Add Dataset
TEST_ADD_DATASET_RESULT_SUCCESS_XML = get_sample("add_dataset_result_success.xml")
TEST_ADD_DATASET_RESULT_SUCCESS_DICTIONARY = get_sample(
    "add_dataset_result_success.json"
)
TEST_ADD_DATASET_RESULT_ERROR_XML = get_sample("add_dataset_result_error.xml")
TEST_ADD_DATASET_RESULT_ERROR_DICTIONARY = get_sample("add_dataset_result_error.json")
TEST_ADD_DATASET_RESULT_GENERIC_SUCCESS_XML = get_sample(
    "add_dataset_result_generic_success.xml"
)
TEST_ADD_DATASET_RESULT_GENERIC_SUCCESS_DICTIONARY = get_sample(
    "add_dataset_result_generic_success.json"
)

# Alter Dataset
TEST_ALTER_DATASET_RESULT_SUCCESS_XML = get_sample("alter_dataset_result_success.xml")
TEST_ALTER_DATASET_RESULT_SUCCESS_DICTIONARY = get_sample(
    "alter_dataset_result_success.json"
)
TEST_ALTER_DATASET_RESULT_ERROR_XML = get_sample("alter_dataset_result_error.xml")
TEST_ALTER_DATASET_RESULT_ERROR_DICTIONARY = get_sample(
    "alter_dataset_result_error.json"
)

# Extract Dataset
TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML = get_sample(
    "extract_dataset_result_base_success.xml"
)
TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_DICTIONARY = get_sample(
    "extract_dataset_result_base_success.json"
)
TEST_EXTRACT_DATASET_RESULT_BASE_ERROR_XML = get_sample(
    "extract_dataset_result_base_error.xml"
)
TEST_EXTRACT_DATASET_RESULT_BASE_ERROR_DICTIONARY = get_sample(
    "extract_dataset_result_base_error.json"
)

# Delete Dataset
TEST_DELETE_DATASET_RESULT_SUCCESS_XML = get_sample("delete_dataset_result_success.xml")
TEST_DELETE_DATASET_RESULT_SUCCESS_DICTIONARY = get_sample(
    "delete_dataset_result_success.json"
)
TEST_DELETE_DATASET_RESULT_ERROR_XML = get_sample("delete_dataset_result_error.xml")
TEST_DELETE_DATASET_RESULT_ERROR_DICTIONARY = get_sample(
    "delete_dataset_result_error.json"
)

# ============================================================================
# Dataset Administration Request Sample Data
# ============================================================================

# Add Dataset
TEST_ADD_DATASET_REQUEST_XML = get_sample("add_dataset_request.xml")
TEST_ADD_DATASET_REQUEST_TRAITS = {
    "datasetname": "ESWIFT.TEST.T1136242.P3020470",
    "uacc": "None",
    "owner": "eswift",
}

# Add Dataset Generic
TEST_ADD_DATASET_REQUEST_GENERIC_XML = get_sample("add_dataset_request_generic.xml")
TEST_ADD_DATASET_REQUEST_GENERIC_TRAITS = {
    "datasetname": "ESWIFT.TEST.**",
    "uacc": "None",
    "owner": "eswift",
    "generic": "yes",
}

# Alter Dataset
TEST_ALTER_DATASET_REQUEST_XML = get_sample("alter_dataset_request.xml")
TEST_ALTER_DATASET_REQUEST_TRAITS = {
    "datasetname": "ESWIFT.TEST.T1136242.P3020470",
    "uacc": "Read",
    "owner": "eswift",
}

# Extract Dataset
TEST_EXTRACT_DATASET_REQUEST_BASE_XML = get_sample("extract_dataset_request_base.xml")
TEST_EXTRACT_DATASET_REQUEST_BASE_TRAITS = {
    "datasetname": "ESWIFT.TEST.T1136242.P3020470"
}

# Delete Dataset
TEST_DELETE_DATASET_REQUEST_XML = get_sample("delete_dataset_request.xml")

# ============================================================================
# Dataset Administration Setters Sample Data
# ============================================================================

TEST_DATASET_SET_UACC_XML = get_sample("dataset_set_uacc.xml")
