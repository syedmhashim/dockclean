import setuptools

with open("requirements.txt", "r") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="docker-clean",
    version="0.0.1",
    author="Muhammad Hashim",
    author_email="hashim.muhammad9@gmail.com",
    description="Tool to clean docker images and containers",
    packages=setuptools.find_packages(),
    install_requires=required,
    scripts=["bin/docker-clean"],
)
