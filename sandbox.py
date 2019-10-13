#!/usr/bin/env python3

import xiaoyi
import os

client = xiaoyi.Client()

client.login(os.environ["TEST_ACCOUNT"], os.environ["TEST_ENCODED_PASSWORD"])

