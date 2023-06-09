# WFU Problem: Backend Server Documentation

This document outlines the endpoints and functionality of the backend server.

## 1. Get User

Returns information about a specific user.

- **Endpoint**: `/getuser`
- **HTTP Method**: GET
- **Request Parameters**:
  - `userid` (string): The unique identifier for the user to retrieve information for.
- **Example Request**: `http://BACKEND_IP_ADDRESS:PORT/getuser?userid=U0001`
- **Example Response**:

```json
{
    "info": {
        "request": "/getuser?userid=U0001",
        "request_type": "/getuser"
    },
    "request": {
        "userid": "U0001"
    },
    "response": {
        "userid": "U0001",
        "username": "WFU Tester",
        "password": "123456",
        "email": "test@wfu.edu",
        "phone_number": "336-123-4567",
        "introduction": "I'm a freshman here at the university. I'm majoring in business and I'm really excited to learn more about entrepreneurship and marketing. In my free time, I love playing basketball, listening to music, and watching movies. I'm also really interested in getting involved in student organizations and volunteering in the community.",
        "skill": ["C++", "JavaScript", "PHP", "Python"],
        "interest": ["hiking", "swimming", "tennis"],
        "group_list": [["G0001", "WFU Problem"], ["G0002", "Weekend Yoga"], ["G0003", "Summer Camp"], ["G0004", "PIT Menu - Ronald"]]
    }
}

```

## 2. Get Group

Returns information about a specific group.

- **Endpoint**: `/getgroup`
- **HTTP Method**: GET
- **Request Parameters**:
  - `groupid` (string): The unique identifier for the group to retrieve information for.
- **Example Request**: `http://BACKEND_IP_ADDRESS:PORT/getgroup?groupid=G0001`
- **Example Response**:

```json
{
    "info": {
        "request": "/getgroup?groupid=G0001",
        "request_type": "/getgroup"
    },
    "request": {
        "groupid": "G0001"
    },
    "response": {
        "groupid": "G0001",
        "group_name": "WFU Problem",
        "user_list": [["U0001", "WFU Tester"], ["U0002", "Madison Brown"], ["U0003", "Emma Davis"], ["U0004", "Emily Thomas"]]
    }
}
```

## 3. Join Group

Assign one user to join one group. This function will check whether this user exists, whether this group exists and whether this user is in this group

- **Endpoint**: `/joingroup`
- **HTTP Method**: GET
- **Request Parameters**:
  - `userid` (string): The unique identifier for the user.
  - `groupid` (string): The unique identifier for the group.
- **Example Request**: `http://BACKEND_IP_ADDRESS:PORT/joingroup?userid=U0001&groupid=G0001`
- **Example Response**:

```json
{
    "info": {
        "request": "/joingroup?userid=U0001&groupid=G0001",
        "request_type": "/joingroup"
    },
    "request": {
        "userid": "U0001",
        "groupid": "G0001"
    },
    "response": {
      "result": 1,
      "status": "Success"
    }
}
```

## 4. Leave Group

Make one user leave one group. This function will check whether this user has already joined this group

- **Endpoint**: `/leavegroup`
- **HTTP Method**: GET
- **Request Parameters**:
  - `userid` (string): The unique identifier for the user.
  - `groupid` (string): The unique identifier for the group.
- **Example Request**: `http://BACKEND_IP_ADDRESS:PORT/leavegroup?userid=U0001&groupid=G0001`
- **Example Response**:

```json
{
    "info": {
        "request": "/leavegroup?userid=U0001&groupid=G0001",
        "request_type": "/leavegroup"
    },
    "request": {
        "userid": "U0001",
        "groupid": "G0001"
    },
    "response": {
      "result": 1,
      "status": "Success"
    }
}
```

## 5. Check Login

Check if one user's email matches this user's password.

- **Endpoint**: `/checklogin`
- **HTTP Method**: GET
- **Request Parameters**:
  - `email` (string): users' login email.
  - `password` (string): password.
- **Example Request**: `http://BACKEND_IP_ADDRESS:PORT/checklogin?email=test@wfu.edu&password=123456`
- **Example Response**:

```json
{
    "info": {
        "request": "/checklogin?email=test@wfu.edu&password=123456",
        "request_type": "/checklogin"
    },
    "request": {
        "email": "test@wfu.edu",
        "password": "123456"
    },
    "response": {
      "result": 1,
    }
}
```

## 6. Get Group List

Returns information about all groups

- **Endpoint**: `/getgrouplist`
- **HTTP Method**: GET
- **Request Parameters**:
  - `keyword` (string): keyword for group_name.
- **Example Request**: `http://BACKEND_IP_ADDRESS:PORT/getgrouplist?keyword=wfu`
- **Example Response**:

```json
{
    "info": {
        "request": "/getgrouplist?keyword=wfu",
        "request_type": "/getgrouplist"
    },
    "request": {
        "keyword": "wfu"
    },
    "response": {
        "result": 1,
        "columns": [
            "groupid",
            "group_name",
            "group_ddl"
        ],
        "group_list": [
            {
                "groupid": "G0001",
                "group_name": "WFU Problem",
                "group_ddl": "2023-05-01 00:00:00"
            }
        ]
    }
}
```

---

# Database Entity-Relationship Diagram
![5961679529234_ pic](https://user-images.githubusercontent.com/90367338/227064603-077321c1-b8c5-4750-b409-ec634d5dd24c.jpg)

