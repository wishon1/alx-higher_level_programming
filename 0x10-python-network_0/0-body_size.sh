#!/bin/bash
# request size of url in bytes
curl -s "$1" | wc -c
