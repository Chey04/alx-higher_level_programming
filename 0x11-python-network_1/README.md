# 0x11. Python - Network #1

## Resources 👀

**Read or watch**:

- [Quickstart with Requests package](https://docs.python-requests.org/en/latest/user/quickstart/)
- [Requests package](https://docs.python-requests.org/en/latest/)
- [Learn to Code with Requests: Working with APIs in Python](https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-requests)
- [What is an API](https://www.webopedia.com/definitions/api/)
- [What is an API? In English, please](https://medium.com/@perrysetgo/what-exactly-is-an-api-in-english-please-b8801d3b3b3d)
- [APIs for Beginners - How to use an API (Full Course / Tutorial)](https://www.youtube.com/watch?v=GZvSYJDk-us)
- [HTTP (HyperText Transfer Protocol)](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [How to Use RESTful APIs with Django](https://www.twilio.com/blog/how-to-use-restful-apis-with-django)
- [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/)

## Tasks

1. [Task 0](./0-hbtn_status.py) - A Python script that fetches a URL using `requests` library.
2. [Task 1](./1-hbtn_header.py) - A Python script that displays the value of a specific response header.
3. [Task 2](./2-post_email.py) - A Python script that sends a POST request with email as a parameter.
4. [Task 3](./3-error_code.py) - A Python script that manages error exceptions in HTTP responses.
5. [Task 4](./4-hbtn_status.py) - A Python script that sends a request and parses the JSON response.
6. [Task 5](./5-hbtn_header.py) - A Python script that sends a request and retrieves a specific response header value.
7. [Task 6](./6-post_email.py) - An advanced version of Task 2, using the `requests` library.
8. [Task 7](./7-error_code.py) - An advanced version of Task 3, using the `requests` library.
9. [Task 8](./8-json_api.py) - A Python script that sends a POST request and searches for a given letter in a JSON API.
10. [Task 9](./9-starwars.py) - A Python script that sends a search request to the Star Wars API.
11. [Task 10](./10-my_github.py) - A Python script that sends a request to the GitHub API to find the user ID of a given username.

## Introduction
This repository contains a series of tasks that are aimed at teaching you how to use Python to handle web requests and process web data.

We will learn how to use the `urllib` module and the `requests` module to send HTTP requests to web servers, and how to process the responses from those servers.

## Tasks
Here are the tasks included in this repository.

### [0. What's my status? #0](./0-hbtn_status.py)
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

### [1. Response header value #0](./1-hbtn_header.py)
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

### [2. POST an email #0](./2-post_email.py)
Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

### [3. Error code #0](./3-error_code.py)
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response. If the HTTP status code is greater than or equal to `400`, the script should print: `Error code:` followed by the value of the HTTP status code.

### [4. What's my status? #1](./4-hbtn_status.py)
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`. Using the package `requests`.

### [5. Response header value #1](./5-hbtn_header.py)
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header, using the package `requests`.

### [6. POST an email #1](./6-post_email.py)
Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response, using the package `requests`.

### [7. Error code #1](./7-error_code.py)
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response. If the HTTP status code is greater than or equal to `400`, the script should print: `Error code:` followed by the value of the HTTP status code, using the package `requests`.

### [8. Search API](./8-json_api.py)
Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter. If no data is provided, print `No result` or `Not a valid JSON` if the JSON is not valid.

### [9. My Github!](./9-starwars.py)
Write a Python script that takes your Github credentials (username and password) and uses the Github API to display your `id`.

### [10. Time for an interview!](./10-my_github.py)
Write a Python script that takes your Github credentials (username and password) and uses the Github API to display your `id`.

## How to Use
To use any of the Python scripts in this repository, you must have Python 3 installed on your machine.

1. Clone this repository
```bash
git clone https://github.com/brainstorma/alx-higher_level_programming.git
```
2. `cd` into the directory of the desired task
```bash
cd alx-higher_level_programming/0x11-python-network_1
```
3. Run the Python script with Python 3
```bash
python3 <filename>
```

## Tasks 📢

### Task 0️⃣

Write a Python script that fetches `https://intranet.hbtn.io/status`

- You must use the package `urllib`
- You are not allowed to import any packages other than `urllib`
- The body of the response must be displayed like the following example (tabulation before -)

```
    - type: <class 'bytes'>
    - content: b'OK'
    - utf8 content: OK
```

### Task 1️⃣

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

- You must use the packages `urllib` and `sys`
- You are not allow to import packages other than `urllib` and `sys`
- The value of this variable is different for each request
- You don’t need to check arguments passed to the script (number or type)
- You must use a `with` statement

### Task 2️⃣

Write a Python script that sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

- The email must be sent in the variable `email`
- You must use the packages `urllib` and `sys`
- You are not allowed to import packages other than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the container provided, using the web server running on port 5000

### Task 3️⃣

Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

- The email must be sent in the variable `email`
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to error check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the container provided, using the web server running on port 5000. The final response must be printed like this:

```
    {"success": true, "email": "guillaume@alx.io"}
```

### Task 4️⃣

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

- You have to manage `urllib.error.HTTPError` exceptions and print: Error code: `XXX` where `XXX` is the HTTP status code, followed by the content of the response (decoded in `utf-8`)
- You must use the packages `urllib` and `sys`
- You are not allowed to import other packages than `urllib` and `sys`
- You don't need to check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the container provided, using the web server running on port 5000

### Task 5️⃣

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header.

- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`
- The value of this variable is different for each request
- You don’t need to check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the container provided, using the web server running on port 5000

### Task 6️⃣

Write a Python script that takes in a URL and a email, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

- The email must be sent in the `email` variable
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to error check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the container provided, using the web server running on port 5000. The final response must be like this: `You got me!`

### Task 7️⃣

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

- If the HTTP status code is greater than or equal to 400, print: `Error code: HTTP_STATUS_CODE`
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the container provided, using the web server running on port 5000

### Task 8️⃣

Write a Python script that fetches `https://intranet.hbtn.io/status`

- You must use the package `requests`
- You are not allow to import packages other than `requests`
- The body of the response must be displayed like the following example (tabulation before -) with one space between the colon and the value like `: `

```
    - type: <class 'str'>
    - content: OK
```

### Task 9️⃣

Write a Python script that takes your Github credentials (username and password) and uses the [Github API](https://developer.github.com/v3/users/#get-the-authenticated-user) to display your `id`

### [10. Time for an interview!](./10-my_github.py)
Write a Python script that takes your Github credentials (username and password) and uses the Github API to display your `id`.

