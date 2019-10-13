import requests
import enum

API_BASE_URL = "https://api.us.xiaoyi.com"


class ErrorCode(enum.Enum):
    OK = 20000

    UNKNOWN_1 = 20203


class APIError(Exception):
    def __init__(self, error_code):
        self.error_code = error_code


class Auth(requests.auth.AuthBase):
    def __init__(self, token, token_secret):
        self.token = token
        self.token_secret = token_secret

    def __call__(self, r):
        return r


class Client(object):
    def __init__(self):
        self.session = requests.Session()
        self.auth = None

    def login(self, account, encoded_password):
        data = self._get(
            "/v4/users/login",
            {"account": account, "password": encoded_password},
            authenticated=False,
        )

        self.auth = Auth(data["token"], data["token_secret"])

    def _get(self, path, params, authenticated=True):
        kwargs = {"params": params.copy()}

        if authenticated:
            kwargs["auth"] = self.auth

        kwargs["params"].update({"seq": 1})

        resp = self.session.get(API_BASE_URL + path, **kwargs).json()

        error_code = ErrorCode(int(resp["code"]))

        if error_code != ErrorCode.OK:
            raise APIError(error_code)

        return resp["data"]
