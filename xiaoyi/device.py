class Device(object):
    def __init__(self, client, data):
        self.client = client

        self.flag = data["flag"]
        self.is_new = data["isNew"]
        self.ipc_param = data["ipcParam"]
        self.message = data["message"]
        self.type = data["type"]
        self.has_pincode = data["hasPincode"]
        self.uid = data["uid"]
        self.password = data["password"]
        self.appParam = data["appParam"]
        self.nickname = data["nickname"]
        self.name = data["name"]
        self.online = data["online"]
        self.share = data["share"]
        self.model = data["model"]
        self.state = data["state"]
        self.category = data["category"]
        self.did = data["did"]
