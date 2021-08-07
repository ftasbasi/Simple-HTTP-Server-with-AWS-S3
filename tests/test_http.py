from nose.tools import assert_true
import requests


def test_request_response():
    url = 'http://localhost:{port}/picus/list'.format(port="5000")

    # Send a request to the mock API server and store the response.
    response = requests.get(url)

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)

def test_request_response2():
    url = 'http://localhost:{port}/picus/list/alican'.format(port="5000")

    # Send a request to the mock API server and store the response.
    response = requests.get(url)

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)