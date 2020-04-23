from setuptools import setup, find_packages
import re


with open("README.rst", "r") as f:
    long_description = f.read()


with open("steam_community_market/__init__.py") as f:
    version = re.search(r"""^__version__\s*=\s*['"]([^\'"]*)['"]""", f.read(), re.MULTILINE).group(1)


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="steam_community_market",
    version=version,
    author="offish",
    author_email="overutilization@gmail.com",
    description="Get item prices and volumes from the Steam Community Market using Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/offish/steam_community_market",
    download_url="https://github.com/offish/steam_community_market/tarball/v" + version,
    packages=["steam_community_market"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=3.6',
)
