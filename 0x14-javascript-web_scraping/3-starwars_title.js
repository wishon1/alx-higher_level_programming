#!/usr/bin/node

// Import the request module
const request = require('request');

// The first argument is the movie ID
const movieId = process.argv[2];

// Construct the API URL using the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  // If there's an error, print it
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const movieData = JSON.parse(body);

  // Print the title of the movie
  console.log(movieData.title);
});
