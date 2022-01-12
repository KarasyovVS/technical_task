import logging
import requests
from urllib.parse import quote_plus


class BaseAPI:
    """
    Base API class for sending requests.

    Attributes
    ----------
    _scheme : str
        Host scheme.
    _host : str
        Base API host to work with.
    _api_version : str
        Version of using API.

    Methods
    -------
    send_get_request(path, params, status_code=None)
        Sends a get-request to API and returns requests.Response object.
        Optional - status code check, if status code is not as expected -
        exception is raised.
    prepare_url(path, params):
        Forms a URL for a request.
    """

    logger = logging.getLogger("BaseAPI")

    def __init__(self, scheme, host, api_version):
        """
        Constructs all the necessary attributes for the BaseAPI object.

        Parameters
        ----------
        scheme : str
            Host scheme.
        host : str
            Base API host to work with.
        api_version : str
            Version of using API.
        """

        self._scheme = scheme
        self._host = host
        self._api_version = api_version

    def send_get_request(self, path: str, params: dict, status_code=None) -> \
            requests.Response:
        """
        Sends a get-request to API and returns requests.Response object.
        Optional - status code check, if status code is not as expected -
        exception is raised.

        By default, status_code is None, that means that status code check is
        disabled.

        Parameters
        ----------
        path : str
            Path for the get-request.
        params : dict
            A dict of required parameters and their values.
        status_code : int
            An expected status code of the response.

        Returns
        -------
        response : requests.Response
            The response from the request.

        Raises
        ------
        RuntimeError
            Raises if response status code is not as expected.
        """

        final_url = self.prepare_url(path, params)
        response = requests.get(final_url)
        if status_code:
            response_status_code = response.status_code
            if response_status_code == status_code:
                self.logger.info("{url_for_logs} - GET - {code}:".format(
                    url_for_logs=final_url.split("?")[0],
                    code=status_code))
            else:
                raise RuntimeError("An error occurred, the status code does not"
                                   " match the expected one: "
                                   "{code} (expected - {expected_code}".
                                   format(code=response_status_code,
                                          expected_code=status_code))
        return response

    def prepare_url(self, path: str, params: dict) -> str:
        """
        Forms a URL for a request.

        Parameters
        ----------
        path : str
            Path for the get-request.
        params : dict
            A dict of required parameters and their values.

        Returns
        -------
        '{}?{}'.format(url, params) : str
            Final url.
        """

        url = "{scheme}://{host}/{api_ver}/{path}".format(
            scheme=self._scheme, host=self._host, api_ver=self._api_version,
            path=path)
        params = "&".join(["{k}={v}".format(
            k=key, v=quote_plus(params[key], ",")) for key in params])
        return "{}?{}".format(url, params)
