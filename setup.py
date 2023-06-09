from pathlib import Path

from setuptools import setup

from checksome import __version__

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Typing :: Typed",
]

if "a" in __version__:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in __version__:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Generates and compares file checksums",
    entry_points={
        "console_scripts": [
            "checksome=checksome.__main__:entry",
        ],
    },
    include_package_data=True,
    install_requires=[
        "cline~=1.0",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="checksome",
    packages=[
        "checksome",
        "checksome.algorithms",
        "checksome.cli",
    ],
    package_data={
        "checksome": ["py.typed"],
        "checksome.algorithms": ["py.typed"],
        "checksome.cli": ["py.typed"],
    },
    python_requires=">=3.9",
    url="https://github.com/cariad/checksome",
    version=__version__,
)
