from nose.tools import assert_true
import requests


def test_request_response():
    url = 'http://127.0.0.1:{port}/picus/list'.format(port="5000")

    # Send a request to the mock API server and store the response.
    response = requests.get(url)
    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)