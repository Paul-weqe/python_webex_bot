import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-webex-bot",
    version="0.1",
    script=["python-webex-bot"],
    author="Paul-weqe",
    author_email="paul1tw1@gmail.com",
    description="a python library that can be used to create Cisco Webex Team bots",
    long_description=long_description,
    long_description_context_type="text/markdown",
    url="https://github.com/Paul-weqe/python-webex-bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)