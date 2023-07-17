---
layout: default
grand_parent: User Admin
parent: Standard
---

# z/OS Unix System Services UID

User administration functions for accessing and modifying a user's z/OS Unix System Services UID. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_omvs_uid()`

```python
def get_omvs_uid(self, userid: str) -> Union[int,None]:
```

#### 📄 Description

Get a user's **z/OS Unix System Services UID**.

#### 📥 Parameters
* `userid`<br>
  The userid of the user who's **z/OS Unix System Services UID** is being requested.

#### 📤 Returns
* `Union[int,None]`<br>
  Returns the user's **z/OS Unix System Services UID** or `None` if the user does not have an **OMVS segment**.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_omvs_uid("squidwrd")
2424
```

## `UserAdmin.set_omvs_uid()`

```python
def set_omvs_uid(self, userid: str, uid: int) -> dict:
```

#### 📄 Description

Change a user's **z/OS Unix System Services UID**.

#### 📥 Parameters
* `userid`<br>
  The userid of the user who's **z/OS Unix System Services UID** is being changed.

* `uid`<br>
  The **z/OS Unix System Services UID** to assign to the specified user.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result Steps dictionary** or a **Concatenated Security Request XML string** if the `UserAdmin.generate_requests_only` class attribute is `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_omvs_uid("squidwrd", 1919)
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  OMVS     (UID         (1919))'}]}, 'returnCode': 0, 'reasonCode': 0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "user": {
        "name": "SQUIDWRD",
        "operation": "set",
        "requestId": "UserRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "ALTUSER SQUIDWRD  OMVS     (UID         (1919))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```