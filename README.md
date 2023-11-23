# django-time-block
an django application to save the timeline information of an object.


## Tutorial
```python
from django_time_block.utils import add_time_block
def format_datetime(date_str: str) -> datetime.datetime:
    """formate datetime string format"""
    return datetime.datetime.strptime(
            date_str,
            "%Y-%m-%d %H:%M:%S",
    ).astimezone(
            timezone.get_current_timezone(),
    )

# record alice's work time according to her clock in record
object_id = "work_time_user_alice"
add_time_block(  # a timeblock record will be created
    object_id=object_id,
    start_datetime=format_datetime("2023-09-01 00:00:00"),
    end_datetime=format_datetime("2023-09-05 00:00:00"),
)
all_include(  # alice didn't work from 2023-09-05 00:00 to 2023-09-06 00:00
    object_id,
    format_datetime("2023-09-02 00:00:00"),
    format_datetime("2023-09-06 00:00:00"),
)  # False
TimeBlock.objects.filter(object_id=object_id).count()  # 1
add_time_block(  # the second record will merged int the first one
    object_id=object_id,
    start_datetime=format_datetime("2023-09-01 00:00:00"),
    end_datetime=format_datetime("2023-09-05 00:00:00"),
)
TimeBlock.objects.filter(object_id=object_id).count()  # 1
all_include(
    object_id,
    format_datetime("2023-09-02 00:00:00"),
    format_datetime("2023-09-06 00:00:00"),
)  # True
```

* For example:
You have to handle a lot of data from 2000-01-01 to 2023-11-11.
    * First day, you may handle the data from 2023-10-01 to 2023-11-11

    * Next day, you may have handled the data from 2023-09-01 to 2023-09-07:
the results look like this:

    > you will record: `2023-09-01~2023-09-07, 2023-10-01~2023-11-11`

    * the third day, you handled the data from 2023-09-06 to 2023-10-02
then, the records will merge into one:

    > this two records will be merged: `2023-09-01 ~ 2023-11-11`



[![PyPI - Version](https://img.shields.io/pypi/v/django-time-block.svg)](https://pypi.org/project/django-time-block)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-time-block.svg)](https://pypi.org/project/django-time-block)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install django-time-block
```

## License

`django-time-block` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
