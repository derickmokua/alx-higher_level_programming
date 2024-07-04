#!/bin/bash
# Sends a request to a URL and outputs the response's status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
