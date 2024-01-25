#!/bin/bash
# Bash script that sends a POST request to the specified URL
# Includes parameters email with the value test@gmail.com and
# subject with the value I will always be here for PLD
curl -s "$1" \
     -X POST \
     -d "email=test@gmail.com&subject=I will always be here for PLD"
