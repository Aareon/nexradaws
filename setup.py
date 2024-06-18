import os
import setuptools

# Read version and author info from ./nexradaws/__init__.py
current_file = __file__
absolute_path = os.path.abspath(current_file)
this_directory = os.path.dirname(absolute_path)
nexradaws_init_path = os.path.join(this_directory, "nexradaws", "__init__.py")

try:
    with open(nexradaws_init_path) as f:
        for l in f.readlines():
            if l.startswith("__authors__"):
                authors = l.split("= ")[1].lstrip("(").rstrip(",)\n").replace("'", "")
            if l.startswith("__version__"):
                version = float(l.split("= ")[1].strip())
except Exception as e:
    raise
#

setuptools.setup(
    name='nexradaws2',
    version=version,
    packages=['nexradaws2','nexradaws2.resources'],
    description= 'Query and download NEXRAD data from AWS S3 storage.',
    long_description= '''This module is designed to allow you to query and download Nexrad
radar files from Amazon Web Services S3 Storage. The real-time feed and full historical archive of original
resolution (Level II) NEXRAD data, from June 1991 to present, is now freely available on Amazon S3 for anyone to use.
More information can be found here https://aws.amazon.com/public-datasets/nexrad/.

If pyart is installed nexradaws allows you to quickly get pyart objects of downloaded files.

nexradaws supports Python 2.7 and Python 3.6.

Github - https://github.com/Aareon/nexradaws

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

**Version 1.1**
* Bug fix for varying filename extensions over the years (.gz .V06 etc). Thanks Nick Guy for the PR!''',
    url='https://github.com/aarande/nexradaws',
    license='MIT',
    author=authors,
    author_email='aaron.anderson74@yahoo.com',
    keywords='weather,radar,nexrad,aws,amazon',
    download_url='https://github.com/Aareon/nexradaws/archive/2.0.tar.gz',
    install_requires=['boto3','pytz','six'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
