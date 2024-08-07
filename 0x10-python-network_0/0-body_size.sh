#!/bin/bash
# Sends a request to a URL using curl and displays the size of the response body.
curl -s "$1" | wc -c

