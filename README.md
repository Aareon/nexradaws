[![Build Status](https://travis-ci.org/Aareon/nexradaws.svg?branch=master)](https://travis-ci.org/Aareon/nexradaws)   [![codecov](https://codecov.io/gh/Aareon/nexradaws/branch/master/graph/badge.svg)](https://codecov.io/gh/Aareon/nexradaws) [![Documentation Status](https://readthedocs.org/projects/nexradaws/badge/?version=latest)](http://nexradaws.readthedocs.io/en/latest/?badge=latest) [![Documentation Status](https://readthedocs.org/projects/nexradaws/badge/?version=devel)](http://nexradaws.readthedocs.io/en/devel/?badge=devel)
# nexradaws
This module is designed to allow you to query and download Nexrad
radar files from Amazon Web Services S3 Storage. The real-time feed and full historical archive of original
resolution (Level II) NEXRAD data, from June 1991 to present, is now freely available on Amazon S3 for anyone to use.
More information can be found here https://aws.amazon.com/public-datasets/nexrad/.

nexradaws supports Python 2.7 and Python 3.6.

Github - https://github.com/Aareon/nexradaws2

PyPi - https://pypi.python.org/pypi/nexradaws2

Docs - http://nexradaws.readthedocs.io/en/latest/

**Required dependencies**

* boto3
* pytz
* six

**Optional dependencies**

* pyart

**Install with pip**::

    pip install nexradaws

New in version 2.0:
* Use `logging` instead of `six` for outputting download progress.
* Perform future time check. Thanks Nick Guy for your fork!

New in version 1.1:
* Bug fix for varying filename extensions over the years (.gz .V06 etc). Thanks Nick Guy for the PR!
