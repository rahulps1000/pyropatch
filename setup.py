import re
import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()

with open('requirements.txt') as fp:
    requirements = [line.strip() for line in fp]

with open('pyropatch/__init__.py') as fp:
    version = re.search('__version__ = "(.+?)"', fp.read())[1]

setuptools.setup(
    name="pyropatch",
    version=version,
    author="Rahul P S",
    author_email="rahulps1000@gmail.com",
    license="LGPLv3+",
    description="An advanced monkeypatcher add-on for Pyrogram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rahulps1000/pyropatch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='~=3.7',
    py_modules=["pyropatch"],
    install_requires=requirements,
)