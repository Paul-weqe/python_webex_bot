#!/bin/bash

 python3 setup.py sdist bdist_wheel
 twine upload -u Paul-weqe -p prep0nd0rate --repository-url https://upload.pypi.org/legacy/ dist/*
