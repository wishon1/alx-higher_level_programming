#!/bin/bash
# script that sends a DELETE request to the specified URL
curl -s "$1" -X DELETE
