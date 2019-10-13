#!/usr/bin/env python3

import xiaoyi
import os
import datetime

client = xiaoyi.Client()

client.login(os.environ["TEST_ACCOUNT"], os.environ["TEST_ENCODED_PASSWORD"])

from_time = datetime.datetime.now() - datetime.timedelta(days=2)
to_time = datetime.datetime.now()
count = 0
for alert in client.alerts(from_time, to_time):
    pic_data = alert.get_picture()
    with open("/tmp/{}.jpg".format(count), "wb") as f:
        f.write(pic_data)

    print(
        "{}: {}".format(
            datetime.datetime.fromtimestamp(alert.time / 1000),
            "/tmp/{}.jpg".format(count),
        )
    )

    count += 1

