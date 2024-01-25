#!/bin/bash
# Sends a request to the specified URL and displays all HTTP
# +methods the server will accept
curl -Is "$1" | grep Allow | cut -c 8-
