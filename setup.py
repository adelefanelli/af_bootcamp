import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='af_bootcamp',
    version='0.0.1',
    author='Adele Fanelli',
    author_email='adele.fanelli@epfl.ch',
    description='Utilities for use in bootcamp.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
