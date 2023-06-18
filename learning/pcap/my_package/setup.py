import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myPkg",
    version="1.0.0",
    author="Emmerson",
    author_email="emmerson@example.com",
    description="My awesome package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages()
)