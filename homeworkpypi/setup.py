from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="text-stats-calculator-pneuma",
    version="0.1.5",
    description="A simple text statistics calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="nailed1",
    author_email="max20070608@gmail.com",
    url="https://github.com/nailed1/culture/tree/feature/docs/homeworkpypi",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT",
)