from nose.tools import assert_true
import requests


def task1_response():
    url = 'http://127.0.0.1:{port}/picus/list'.format(port="5000")

    # Send a request to the mock API server and store the response.
    response = requests.get(url)
    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)

def task2_response():
    payload = {"textfile.py","print(123)"}
    r = requests.post('https://httpbin.org/post', data=payload)
    assert_true("textfile.py")

def task3_response():
    url = 'http://127.0.0.1:{port}/picus/list/sample1.txt'.format(port="5000")

    # Send a request to the mock API server and store the response.
    response = requests.get(url)
    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)