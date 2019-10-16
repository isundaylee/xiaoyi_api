import cryptography.hazmat.primitives.ciphers
import cryptography.hazmat.backends


class Alert(object):
    def __init__(self, client, data):
        self.client = client

        self.uid = data["uid"]
        self.video_pwd = data["video_pwd"]
        self.sub_type = data["sub_type"]
        self.name = data["name"]
        self.pic_urls = data["pic_urls"]
        self.video_urls = data["video_urls"]
        self.time = data["time"]
        self.type = data["type"]
        self.message = data["message"]
        self.category = data["category"]
        self.pic_pwd = data["pic_pwd"]

    def get_picture(self):
        return self._get_and_decrypt(self.pic_urls, self.pic_pwd)

    def get_video(self):
        return self._get_and_decrypt(self.video_urls, self.video_pwd)

    def _get_and_decrypt(self, url, pwd):
        encrypted_data = self.client.session.get(url).content
        encrypted_data = encrypted_data[4:]

        backend = cryptography.hazmat.backends.default_backend()
        key = pwd.encode()
        iv = bytes([0] * 16)
        cipher = cryptography.hazmat.primitives.ciphers.Cipher(
            cryptography.hazmat.primitives.ciphers.algorithms.AES(key),
            cryptography.hazmat.primitives.ciphers.modes.ECB(),
            backend=backend,
        )

        decryptor = cipher.decryptor()
        data = decryptor.update(encrypted_data) + decryptor.finalize()

        return data

