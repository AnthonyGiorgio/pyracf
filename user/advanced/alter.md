---
layout: default
grand_parent: User Admin
parent: Advanced
---

# Alter

Alter an existing z/OS userid.
{: .fs-6 .fw-300 }

## `UserAdmin.alter()`

```python
def alter(self, userid: str, traits: dict = {}) -> dict:
```

#### 📄 Description

Alter an existing **z/OS userid**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** being altered.

* `traits`<br>
  A dictionary of **traits/attributes** that should be altered. See [Traits](../segments_traits_operators#traits) to see what all of the valid **User Traits** are.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result dictionary** or a **Security Request XML string** if the `UserAdmin.generate_request_only` class attribute is `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **alters** a user with a userid of `squidwrd` and **traits/attributes** to alter are specified in the `traits` dictionary.


###### Python Script

```python
from pyracf import UserAdmin
user_admin = UserAdmin()

traits = {
    "base:special": False,
    "base:operations": True,
    "omvs:home": "/u/clarinet",
    "omvs:program": False,
}

user_admin.alter("squidwrd", traits=traits)
```

###### Security Result Dictionary as JSON
```json
{
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
          "image": "ALTUSER SQUIDWRD  NOSPECIAL      OPERATIONS   OMVS     (HOME        ('/u/clarinet') NOPROGRAM     )"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```