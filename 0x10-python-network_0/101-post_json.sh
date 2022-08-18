#!/bin/bash
# send JSON POST request to a URL
curl -s -X POST "$1" -H "Content-Type: application/json" -d "$(cat $2)"
