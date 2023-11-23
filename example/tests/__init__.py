# SPDX-FileCopyrightText: 2023-present Xiang Wang <ramwin@qq.com>
#
# SPDX-License-Identifier: MIT


"""
unittest
"""


import datetime
import unittest

from django.test import TestCase
from django.utils import timezone

from django_time_block.models import TimeBlock
from django_time_block.utils import add_time_block


class FunctionTestCase(TestCase):
    """
    test time block function
    """

    def test_add_time_block(self):
        """
        base
        """
        object_id = "work_time_user_alice"
        add_time_block(
                object_id=object_id,
                start_datetime=datetime.datetime(
                    2023, 9, 1, 0, 0, 0,
                    tzinfo=timezone.get_current_timezone()
                ),
                end_datetime=datetime.datetime(
                    2023, 9, 7, 0, 0, 0,
                    tzinfo=timezone.get_current_timezone()
                ),
        )
