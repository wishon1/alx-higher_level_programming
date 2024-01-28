#!/usr/bin/bash
# script for performing a JSON POST request using a specified JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
