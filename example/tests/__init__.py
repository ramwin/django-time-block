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
from django_time_block.utils import add_time_block, all_include, get_gap


def format_datetime(date_str: str) -> datetime.datetime:
    """formate datetime string format"""
    return datetime.datetime.strptime(
            date_str,
            "%Y-%m-%d %H:%M:%S",
    ).astimezone(
            timezone.get_current_timezone(),
    )


class FunctionTestCase(TestCase):
    """
    test time block function
    """

    def test_add_time_block(self):
        """base"""
        object_id = "work_time_user_alice"
        add_time_block(
            object_id=object_id,
            start_datetime=format_datetime("2023-09-01 00:00:00"),
            end_datetime=format_datetime("2023-09-05 00:00:00"),
        )
        self.assertFalse(all_include(
            object_id,
            format_datetime("2023-09-02 00:00:00"),
            format_datetime("2023-09-06 00:00:00"),
        ))
        add_time_block(
            object_id=object_id,
            start_datetime=format_datetime("2023-09-05 00:00:00"),
            end_datetime=format_datetime("2023-09-07 00:00:00"),
        )
        self.assertEqual(TimeBlock.objects.count(), 1)
        self.assertTrue(all_include(
            object_id,
            format_datetime("2023-09-02 00:00:00"),
            format_datetime("2023-09-06 00:00:00"),
        ))

    def test_get_gap(self):
        """test_get_gap"""
        object_id = "work_time_user_bob"
        add_time_block(
            object_id=object_id,
            start_datetime=format_datetime("2023-09-01 00:00:00"),
            end_datetime=format_datetime("2023-09-02 00:00:00"),
        )
        add_time_block(
            object_id=object_id,
            start_datetime=format_datetime("2023-09-03 00:00:00"),
            end_datetime=format_datetime("2023-09-04 00:00:00"),
        )
        self.assertTrue(
            get_gap(
                object_id,
                format_datetime("2023-09-02 11:00:00"),
                format_datetime("2023-09-03 11:00:00"),
            ),
            format_datetime("2023-09-02 11:00:00"),
        )
        self.assertTrue(
            get_gap(
                object_id,
                format_datetime("2023-09-01 11:00:00"),
                format_datetime("2023-09-03 11:00:00"),
            ),
            format_datetime("2023-09-02 00:00:00"),
        )
        add_time_block(
            object_id=object_id,
            start_datetime=format_datetime("2023-09-01 00:00:00"),
            end_datetime=format_datetime("2023-09-04 00:00:00"),
        )
        self.assertEqual(TimeBlock.objects.count(), 1)
