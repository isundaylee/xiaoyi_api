class Alert(object):
    def __init__(self, client, data):
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

