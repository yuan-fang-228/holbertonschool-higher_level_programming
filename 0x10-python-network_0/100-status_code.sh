#!/bin/bash
# send a request and only display the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
