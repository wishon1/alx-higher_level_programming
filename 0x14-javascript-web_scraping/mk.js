#!/usr/bin/node

// Import the request module
const request = require('request');

// Extract the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Make an HTTP GET request to the API
request(apiUrl, (error, response, body) {
  // Check if there is error
  if (error) {
    console.error(error)
  } else {
    // Parse the JSON response
    const films = JSON.parse(body).results;

    // Count the number of movies where character "Wedge Antilles" is present
    const moviesWithWedge = films.reduce((count, film) => {
      // Check if "Wedge Antilles" is present in the list of characters
      return film.characters.find((character) => character.endsWith('/18/'))
        ? count + 1 // Increment count if found
        : count;    // Keep count unchanged if not found
    }, 0);          // Initialize count to zero

    // Print the number of movies where "Wedge Antilles" is present
    console.log(moviesWithWedge);
  }
});
