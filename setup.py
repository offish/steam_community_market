import re
from pathlib import Path
from setuptools import setup

base_dir = Path(__file__).resolve().parent
init_file = base_dir / "steam_community_market" / "__init__.py"
readme_file = base_dir / "README.rst"

with open(init_file, "r") as f:
    version = re.search(
        r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", f.read(), re.MULTILINE
    )[1]

long_description = readme_file.read_text()

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
    download_url=f"https://github.com/offish/steam_community_market/tarball/v{version}",
    packages=["steam_community_market"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    python_requires=">=3.6",
)
