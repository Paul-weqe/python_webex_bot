import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_webex_bot",
    version="0.3",
    script=["python_webex_bot"],
    author="Paul-weqe",
    author_email="paul1tw1@gmail.com",
    description="a python library that can be used to create Cisco Webex Team bots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Paul-weqe/python_webex_bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
