#!/usr/bin/env python3

import xiaoyi
import os
import datetime

client = xiaoyi.Client()

client.login(os.environ["TEST_ACCOUNT"], os.environ["TEST_ENCODED_PASSWORD"])

from_time = datetime.datetime.now() - datetime.timedelta(days=1)
to_time = datetime.datetime.now()
for alert in client.alerts(from_time, to_time):
    print(datetime.datetime.fromtimestamp(alert.time / 1000))
