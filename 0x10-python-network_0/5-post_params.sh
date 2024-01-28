#!/bin/bash
# Bash script that sends a POST request to the specified URL
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
