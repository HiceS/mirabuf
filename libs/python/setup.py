import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
# README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mirabuf",
    version="1.0.0",
    description="3D file format for physical assemblies",
    long_description_content_type="text/markdown",
    url="https://github.com/HiceS/mirabuf",
    author="HiceS",
    author_email="shawnhice@gmail.com",
    license="BSD 3",
    classifiers=[
        "License :: BSD 3 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["mirabuf"],
    install_requires=["protobuf"],
)