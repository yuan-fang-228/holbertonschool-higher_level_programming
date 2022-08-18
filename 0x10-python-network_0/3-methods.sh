#!/bin/bash
# display all HTTP methods of the server
curl -s -i "$1" | grep "Allow:" | cut -d " " -f2-
