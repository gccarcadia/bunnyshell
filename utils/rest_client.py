import requests
import json


class RestClient():
    """
    This class represents a REST client
    """

    def __init__(self):
        pass

    def api_call(self, host_url, http_method, request_data=None):
        """
        Method to create a REST API call
        """

        supported_http_methods = ["POST", "GET", "PUT", "DELETE"]
        if http_method not in supported_http_methods:
            raise ValueError(f"{http_method} method not supported: Current "
                f"supported methods: {supported_http_methods}")

        if http_method == "POST":
            # response = requests.post(host_url, data=json.dumps(request_data))
            response = requests.post(host_url, data=request_data)
        elif http_method == "GET":
            response = requests.get(host_url)
        elif http_method == "PUT":
            # response = requests.put(host_url, data=json.dumps(request_data))
            response = requests.put(host_url, data=request_data)
        elif http_method == "DELETE":
            # response = requests.delete(host_url, data=json.dumps(request_data))
            response = requests.delete(host_url)

        if (response.content and response.status_code) is None:
            raise Exception(
                f"Request to {host_url}, action {http_method} failed with error"
                f" {response.status_code}"
            )

        return response
