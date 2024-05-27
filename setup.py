#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    INSTALL_REQUIRES = [pytest >= 8.2.1]

    setuptools.setup(
            name="Scuttler",
            version="0.0.1",
            author="Ólavur Mortensen",
            author_email="olavurmortensen@gmail.com",
            description="Scuttler -- Hexapod robot",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/olavurmortensen/scuttler",
            packages=setuptools.find_packages(),
            install_requires=INSTALL_REQUIRES,
            python_requires='>=3.8',
            )
