#!/bin/sh
 
# Python
source pyenv/bin/activate

# Server
export FLASK_DEBUG=1
export FLASK_APP=server
flask run