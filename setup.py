
import os
from setuptools import setup

REQUIREMENTS = [
]
README = os.path.join(os.path.dirname(__file__), 'README.md')
LONG_DESCRIPTION = open(README, 'r').read()
CLASSIFIERS = [
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
]

setup(
    name="ringcaptcha",
    version=VERSION,
    author="Martin Cocaro",
    author_email="martin@ringcaptcha.com",
    description="Provides simplified interaction with the Ringcaptcha verification REST API.",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/dfejgelis/ringcaptcha-python",
    packages=("ringcaptcha",),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    zip_safe=False,
)
