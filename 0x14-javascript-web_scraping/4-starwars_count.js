#!/usr/bin/node

// Import the request module
const request = require('request');

// The API URL of the Star Wars API films endpoint
const apiUrl = process.argv[2];

// Character ID of "Wedge Antilles"
const characterId = 18;
const url = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

// Make a request to the films endpoint
request(apiUrl, (error, response, body) => {
  // If there's an error, print it
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const filmsData = JSON.parse(body);

  // Initialize a counter for the number of movies with "Wedge Antilles"
  let movieCount = 0;

  // Loop through each film
  filmsData.results.forEach(film => {
    // Check if "Wedge Antilles" is present in the list of characters
    if (film.characters.includes(url)) {
      movieCount++;
    }
  });

  // Print the number of movies where "Wedge Antilles" is present
  console.log(movieCount);
});
