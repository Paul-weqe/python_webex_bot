import setuptools

required = None
with open('requirements.txt') as f:
    required = f.read().splitlines()


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_webex_bot",
    version="0.74",
    scripts=["python_webex_bot"],
    author="Paul-weqe",
    author_email="paul1tw1@gmail.com",
    description="Introducing detection of incoming file submissions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Paul-weqe/python_webex_bot",
    packages=setuptools.find_packages(),
    install_requires=[
        "atomicwrites",
        "attrs",
        "backcall",
        "certifi",
        "chardet",
        "Click",
        "colorama",
        "coverage",
        "decorator",
        "Flask",
        "idna",
        "itsdangerous",
        "jedi",
        "Jinja2",
        "MarkupSafe",
        "more-itertools",
        "parso",
        "pickleshare",
        "pluggy",
        "prompt-toolkit",
        "py",
        "Pygments",
        "pytz",
        "requests",
        "six",
        "traitlets",
        "urllib3",
        "virtualenv",
        "wcwidth",
        "Werkzeug"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)

