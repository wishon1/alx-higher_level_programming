#!/usr/bin/bash
# request to 0.0.0.0:5000/catch_me gets "You got me!" in the response.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
