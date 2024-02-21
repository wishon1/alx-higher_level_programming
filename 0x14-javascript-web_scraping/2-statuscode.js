#!/usr/bin/node

// import the request module for sending request
const request = require('request');

// first argument is the URL to request (GET)
const url = process.argv[2];

// make http Get request to the url
request(url, (error, response) => {
  // if there is an error print it
  if (error) {
    console.error(error);
    return;
  }

  // print the status code
  console.log('code:', response.statusCode);
});
