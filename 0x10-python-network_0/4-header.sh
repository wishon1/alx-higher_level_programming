#!/bin/bash
# Bash script that sends a GET request to the specified URL,
# --includes the header X-School-User-Id with the value 98,
# --and displays the response body
curl -s "$1" -H "X-School-User-Id: 98"
