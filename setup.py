from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES = [
    "georss_client>=0.14",
]

setup(
    name="georss_nrcan_earthquakes_client",
    version="0.3",
    author="Malte Franken",
    author_email="coding@subspace.de",
    description="A GeoRSS client library for the Natural Resources Canada Earthquakes feed.",
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/exxamalte/python-georss-nrcan-earthquakes-client",
    packages=find_packages(exclude=("tests*",)),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES,
)
