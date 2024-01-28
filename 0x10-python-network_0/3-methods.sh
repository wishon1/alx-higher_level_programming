#!/bin/bash
# Sends a request to the specified URL and displays all HTTP
curl -Is "$1" | grep Allow | cut -c 8-
