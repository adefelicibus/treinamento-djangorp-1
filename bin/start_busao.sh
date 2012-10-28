#!/bin/bash

export PYTHONPATH="/home/python/src/busao/:/home/python/.virtualenvs/busao/lib/python2.7/site-packages/"

/home/python/.virtualenvs/busao/bin/gunicorn_django busao.settings
