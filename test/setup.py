from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ndfl-nailed1",
    version="0.0.0",
    author="nailed1",
    description="Python-пакет для работы с НДФЛ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nailed1/culture/tree/feature/makeutil/test",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)