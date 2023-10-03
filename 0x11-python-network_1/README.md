### Learning objectives
#### Python Internet Resource Retrieval and Data Manipulation
In Python, you can fetch internet resources and manipulate data from external services using different packages. Two commonly used packages are urllib and requests. In this guide, we'll explore both methods.

#### Fetching Internet Resources with urllib
Making an HTTP GET Request
To fetch internet resources using the urllib package, you can use the following steps:

Import the urllib.request module.

```python
import urllib.request
```
Make an HTTP GET request and retrieve the response content.

```python
url = 'https://example.com'
response = urllib.request.urlopen(url)
html = response.read()
```
Decoding urllib Response
You can decode the response content as needed, depending on the encoding used by the server. For example, to decode the response as UTF-8:

```python
decoded_html = html.decode('utf-8')
```
Using the Python package requests
The requests package is a popular choice for making HTTP requests in Python due to its simplicity.

Making an HTTP GET Request
To make an HTTP GET request using requests, follow these steps:

Install the requests library if you haven't already:

```bash
pip install requests
```
Import the requests module.

```python
import requests
```
Make an HTTP GET request and retrieve the response content:

```python
url = 'https://example.com'
response = requests.get(url)
html = response.text
```
Making HTTP POST/PUT/etc. Requests
You can use requests for various types of requests (POST, PUT, etc.) by using the appropriate methods like requests.post() or requests.put(). Provide the necessary data and parameters as required.

#### Fetching JSON Resources
To fetch JSON resources and automatically decode them, use requests:

```python
url = 'https://example.com/api/data.json'
response = requests.get(url)
data = response.json()
```
#### Manipulating Data from an External Service
Once you have retrieved data from an external service, you can manipulate it as needed based on the data structure returned in the response. For example, if you fetched JSON data, you can access and manipulate the data in Python.

```python
# Assuming 'data' is a JSON response
value = data['key']
# Perform further data manipulation as needed
.....................
```
