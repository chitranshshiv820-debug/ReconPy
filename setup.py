# setup.py

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_desc = f.read()

setup(
    name="reconpy",
    version="1.0.0",
    description="ReconPy - OSINT-inspired website security scanner",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="Chitransh",
    author_email="chitranshshiv820@gmail.com",
    url="https://github.com/chitranshshiv820-debug/ReconPy",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0",
        "pyfiglet>=0.8.post1",
        "colorama>=0.4.6",
        "PyYAML>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "reconpy=scanner:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
)
