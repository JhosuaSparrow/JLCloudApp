# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file      :test.py
@author    :Jack Sun (jack.sun@quectel.com)
@brief     :<description>
@version   :1.0.0
@date      :2023-11-28 15:30:43
@copyright :Copyright (c) 2023
"""

import utime as time
from tp import gt9xx
from machine import Pin

tp_gt911 = gt9xx(irq=40, reset=20)
res = tp_gt911.activate()
res = tp_gt911.init()
gpio40 = Pin(Pin.GPIO40, Pin.OUT, Pin.PULL_PU, 0)
print("gpio40.read():", gpio40.read())

while 1:
    print("tp_gt911.read_xy():", tp_gt911.read_xy())
    time.sleep_ms(100)
