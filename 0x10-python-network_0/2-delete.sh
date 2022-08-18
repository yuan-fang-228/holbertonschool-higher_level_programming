#!/bin/bash
# send a delete request to URL passed and display the body response
curl -s -X DELETE "$1"
