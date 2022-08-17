#!/bin/bash
# display the body size of the reponose
curl -s -i "$1" | grep Content-Length: | cut '-d ' '-f2'
