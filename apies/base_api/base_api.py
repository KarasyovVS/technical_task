import logging
import sys

import requests


class BaseAPI:
    """
    Base API class for sending requests.

    Attributes
    ----------
    _scheme : str
        Host scheme.
    _host : str
        Base API host to work with.
    _api_ver : str
        Version of using API.

    Methods
    -------
    send_get_request(path, params, status_code)
        Sends a get-request to API and returns response dictionary object.
        Optional - status code check, if status code is not as expected -
        exception is raised.
    get_status_code(response)
        Returns the status code from the 'response' variable.
    get_info_from_json(response)
        Returns the JSON as a dict object from the 'response' variable.
    prepare_url(path, params) -> str:
        Forms a URL for request.
    """

    logger = logging.getLogger("BaseAPI")

    def __init__(self, scheme, host, api_version):
        self._scheme = scheme
        self._host = host
        self._api_ver = api_version

    def send_get_request(self, path: str, params: dict, status_code: int) -> \
            dict:
        """
        Sends a get-request to API and returns response dictionary object.
        Optional - status code check, if status code is not as expected -
        exception is raised.

        Parameters
        ----------
        path : str
            Path for the get-request.
        params : dict
            A dict of required parameters and their values.
        status_code : int
            An expected status code or the response.

        Returns
        -------
        get_info_from_json(response) : dict
            Dictionary with data taken from the response.

        Raises
        ------
        SystemExit
            Raises if response status code is not as expected.
        """

        final_url = self.prepare_url(path, params)
        response = requests.get(final_url)
        if status_code:
            response_status_code = self.get_status_code(response)
            if response_status_code == status_code:
                self.logger.info("{url_for_logs} - GET - {code}:".format(
                    url_for_logs=final_url.split("?")[0],
                    code=status_code))
            else:
                self.logger.error("An error occurred, status code: {code}".
                                  format(code=response_status_code))
                sys.exit()
        return self.get_info_from_json(response)

    def get_status_code(self, response: requests.Response) -> int:
        """
        Returns the status code from the 'response' variable.

        Returns
        -------
        response.status_code : int
            Value of response status code.
        """

        return response.status_code

    def get_info_from_json(self, response: requests.Response) -> dict:
        """
        Returns the JSON as a dict object from the 'response' variable.

        Returns
        -------
        response.json() : dict
            JSON as a 'dict' python object.
        """

        return response.json()

    def prepare_url(self, path: str, params: dict) -> str:
        """
        Forms a URL for request.

        Parameters
        ----------
        path : str
            Path for the get-request.
        params : dict
            A dict of required parameters and their values.

        Returns
        -------
        "&".join([url, *params]) : str
            Final url.
        """

        url = "://".join([self._scheme, "/".join([self._host, self._api_ver,
                                                  path])])
        params = ["=".join([key, params[key]]) for key in params]
        return "&".join([url, *params])
