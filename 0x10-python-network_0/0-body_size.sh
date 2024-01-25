#!/bin/bash
# Sends a request to the specified URL and displays the size of
# +the response body in bytes
curl -s "$1" | wc -c
