# setup.py

from setuptools import setup, find_packages

setup(
    name="reconpy",
    version="1.0.0",
    description="ReconPy – OSINT-inspired website security scanner",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Chitransh",  # Replace with your name
    author_email="chitranshshiv820@gmail.com",  # Replace with your email
    url="https://github.com/chitranshshiv820-debug/ReconPy",  # Replace with your GitHub repo link
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "pyfiglet",
        "colorama",
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "reconpy=scanner:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Security",
        "Topic :: Utilities"
    ],
    python_requires=">=3.7",
)
