#!/bin/bash
# Sends a POST request with JSON data to a URL and prints the response body.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
