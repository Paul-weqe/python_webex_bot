import setuptools

required = None
with open('requirements.txt') as f:
    required = f.read().splitlines()


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_webex_bot",
    version="0.901",

    scripts=["python_webex_bot"],
    author="Paul-weqe",
    description="Enable sending markdown in messges",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Paul-weqe/python_webex_bot",
    packages=setuptools.find_packages(),
    install_requires=[
        "certifi",
        "chardet",
        "click",
        "Flask",
        "idna",
        "itsdangerous",
        "Jinja2",
        "MarkupSafe",
        "requests",
        "urllib3",
        "Werkzeug"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
