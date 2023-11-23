# django-time-block
an django application to save the timeline information of an object.


## Tutorial
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
