#!/bin/bash
# Sends a request to the endpoint at 0.0.0.0:5000/catch_me and expects a response with the message "You got me!".
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
