#!/bin/bash
# Bash script that sends a DELETE request to the specified URL
# +and displays the response body
curl -s "$1" -X DELETE
