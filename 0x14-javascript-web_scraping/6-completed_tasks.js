#!/usr/bin/node

// Import the request module
const request = require('request');

// Extract the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Create a dictionary to store the count of completed tasks per user
const completedTasksPerUser = {};

// Make an HTTP GET request to the API URL
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const tasksData = JSON.parse(body);

    // Iterate through each task
    tasksData.forEach(function (task) {
      // Check if the task is completed
      if (task.completed === true) {
        // Extract the user ID of the task owner
        const userId = task.userId;

        // Increment the count of completed tasks for the user
        if (!(userId in completedTasksPerUser)) {
          completedTasksPerUser[userId] = 0;
        }
        completedTasksPerUser[userId] += 1;
      }
    });

    // Print the dictionary containing the count of completed tasks per user
    console.log(completedTasksPerUser);
  }
});
