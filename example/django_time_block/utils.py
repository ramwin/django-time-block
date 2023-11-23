#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
utils to handle the time block
"""


from .models import TimeBlock


def set_include(object_id: str, start_datetime, end_datetime):
    """
    first scenerio:
        the old time block contains new timeblock
        ===========  old time
          ----       new time

    second scenerio:
        ==== == ====  old time
          -------     new time

    third scenerio:
        ====     ===  old time
             ---      new time
    """
    # first sceneraio
    queryset = TimeBlock.objects.filter(object_id=object_id)
    if queryset.filter(
            start_datetime__lte=start_datetime,
            end_datetime__gte=end_datetime).exists():
        return
    new_timeblock = TimeBlock.objects.create(
            object_id=object_id,
            start_datetime=start_datetime,
            end_datetime=end_datetime
    )
    # merge the overlap timeblock
    queryset.filter(
            start_datetime__gte=new_timeblock.start_datetime,
            end_datetime__lte=new_timeblock.end_datetime,
    ).exclude(id=new_timeblock.id).delete()
    # pylint: disable=pointless-string-statement
    """
    now, there is not time block in the new time, we can extend the front overlap
    and end overlap timeblock
    =======     ========  old time
         ---------        new time
         |      |
       front    |
      overlap   |
               end
             overlap
    """
    front_overlap = queryset.filter(
            start_datetime__lt=new_timeblock.start_datetime,
            end_datetime__gte=new_timeblock.start_datetime,
    ).first()
    if front_overlap:
        front_overlap.end_datetime = new_timeblock.end_datetime
        front_overlap.save()
    end_overlap = queryset.filter(
            start_datetime__lte=new_timeblock.end_datetime,
            end_datetime__gt=new_timeblock.end_datetime,
    )
    if end_overlap:
        end_overlap.start_datetime = new_timeblock.start_datetime
        end_overlap.save()
    if front_overlap or end_overlap:
        new_timeblock.delete()
    if front_overlap and end_overlap:
        front_overlap.end_datetime = end_overlap.end_datetime
        front_overlap.save()
        end_overlap.delete()
