import requests
import enum
import hashlib
import hmac
import base64
import json

from .device import Device

API_BASE_URL = "https://api.us.xiaoyi.com"


class ErrorCode(enum.Enum):
    OK = 20000

    HMAC_MISSING = 20201
    HMAC_INVALID = 20202

    UNKNOWN_1 = 20203


class APIError(Exception):
    def __init__(self, error_code):
        self.error_code = error_code


class Auth(requests.auth.AuthBase):
    def __init__(self, token, token_secret):
        self.token = token
        self.token_secret = token_secret

    def __call__(self, r: requests.PreparedRequest):
        r.prepare_url(r.url, "hmac={}".format(self._get_hmac(r).replace("=", "%3D")))
        return r

    def _get_hmac(self, r: requests.PreparedRequest) -> str:
        path = r.path_url
        query = path[path.find("?") + 1 :]
        query = "&".join(sorted(query.split("&")))

        key = "{}&{}".format(self.token, self.token_secret)

        digester = hmac.new(key.encode(), query.encode(), hashlib.sha1)
        return base64.b64encode(digester.digest()).decode()


class Client(object):
    def __init__(self):
        self.session = requests.Session()

        self.auth = None
        self.userid = None

    def login(self, account, encoded_password):
        data = self._get(
            "/v4/users/login",
            {"account": account, "password": encoded_password},
            authenticated=False,
        )

        self.auth = Auth(data["token"], data["token_secret"])
        self.userid = data["userid"]

    def devices(self):
        data = self._get("/v4/devices/list", {"userid": self.userid})

        return list(map(lambda entry: Device(self, entry), data))

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
