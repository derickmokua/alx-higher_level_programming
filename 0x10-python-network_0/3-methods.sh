#!/bin/bash
# Displays all HTTP methods that the server will accept using curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
