import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="steam_community_market",
    version="1.0.0",
    author="offish",
    author_email="overutilization@gmail.com",
    description="Easily get item prices and volumes from the Steam Community Market using Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/offish/steam_community_market",
    download_url='https://github.com/offish/steam_community_market/archive/v1.0.0.tar.gz',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
