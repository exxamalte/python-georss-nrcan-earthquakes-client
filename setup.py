from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = "georss_nrcan_earthquakes_client"
AUTHOR = "Malte Franken"
AUTHOR_EMAIL = "coding@subspace.de"
DESCRIPTION = (
    "A GeoRSS client library for the Natural Resources Canada Earthquakes feed."
)
URL = "https://github.com/exxamalte/python-georss-nrcan-earthquakes-client"

REQUIRES = [
    "georss_client>=0.14",
]

setup(
    name=NAME,
    version="0.3",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=find_packages(exclude=("tests*",)),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES,
)
