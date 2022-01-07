import requests


class BaseAPI:
    """
    Base API class for sending requests

    ...

    Attributes
    ----------
    _url : str
        Base API url to work with.

    Methods
    -------
    send_get_request(path='')
        Sends a get-request to API and saves a response from API as a class
        attribute named '_response'.
    """

    def __init__(self, url: str):
        """
        Constructs all the necessary attributes for the BaseAPI object.

        Parameters
        ----------
        url : str
            Base API url to work with.
        """

        self._url = url

    def send_get_request(self, path=""):
        """
        Sends a get-request to API and saves a response from API as a class
        attribute named '_response'.

        If the argument 'path' is passed, then the get-request is sent to url.

        Parameters
        ----------
        additional path : str, optional
            Path for the get-request.

        Returns
        -------
        None
        """

        self._response = requests.get("/".join([self._url, path]))
