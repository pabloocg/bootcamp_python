#!/bin/bash
python3.7 setup.py sdist

pip3 install ./dist/ai42-1.0.0.tar.gz

rm -r dist/ ai42.egg-info
