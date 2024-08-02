#!/usr/bin/env bash

apt-get install -y python3 python3-pip python3-dev

# install necessary packages
pip install --no-cache-dir --upgrade pip 


pip install -r /autograder/source/requirements.txt
