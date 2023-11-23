# SPDX-FileCopyrightText: 2023-present Xiang Wang <ramwin@qq.com>
#
# SPDX-License-Identifier: MIT


import datetime
import unittest

from django.test import TestCase
from django.utils import timezone

from django_time_block.models import TimeBlock
from django_time_block.utils import add_time_block


class FunctionTestCase(TestCase):

    def test1(self):
        object_id = "work_time_user_alice"
        TimeBlock.objects.create(
                object_id=object_id,
                start_datetime=datetime.datetime(
                    timezone.get_current_timezone()
        )
