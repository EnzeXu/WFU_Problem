WFU Problem
===========================

# Backend Server Documentation

This document outlines the endpoints and functionality of the backend server.

## 1. Get User

Returns information about a specific user.

- **Endpoint**: `/getuser`
- **HTTP Method**: GET
- **Request Parameters**:
  - `userid` (string): The unique identifier for the user to retrieve information for.
- **Example Request**: `http://18.117.181.47:8888/getuser?userid=U0001`
- **Example Response**:

```json
{
    "info": {
        "request": "/getuser?userid=0001",
        "request_type": "/getuser"
    },
    "request": {
        "userid": "0001"
    },
    "response": {
        "userid": "0001",
        "username": "Madison Brown",
        "password": "mb123456",
        "email": "mb@gmail.com"
    }
}
```


