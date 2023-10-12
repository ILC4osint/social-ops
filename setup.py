from setuptools import setup, find_packages

setup(
    name="socint",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pydantic",
        "argparse",
        # add other dependencies
    ],
    entry_points={
        "console_scripts": [
            "socint = socint.cli:main",
        ],
    },
)