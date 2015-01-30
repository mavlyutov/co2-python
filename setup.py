#!/usr/bin/env python
import setuptools


setuptools.setup(
    name="co2-python",
    version="1.0",
    description="CO2 Monitor",
    author="Marat Mavlyutov",
    author_email="mavlyutov@yandex-team.ru",
    url="http://wiki.yandex-team.ru/",
    packages=["co2_monitor"],
    install_requires=["pyusb >= 1.0.0b2"],
    include_package_data=True
)
