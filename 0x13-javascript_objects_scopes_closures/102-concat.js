#!/usr/bin/node

const fs = require('fs').promises;

/**
 * Concatenates the contents of two input files and writes the result to an output file.
 * @param {string} inputPathA - Path to the first input file.
 * @param {string} inputPathB - Path to the second input file.
 * @param {string} outputPath - Path to the output file.
 */
async function concatenateFiles (inputPathA, inputPathB, outputPath) {
  try {
    // Read the contents of the first input file.
    const dataA = await fs.readFile(inputPathA, 'utf8');

    // Read the contents of the second input file.
    const dataB = await fs.readFile(inputPathB, 'utf8');

    // Concatenate the data from both files.
    const concatenatedData = dataA + dataB;

    // Write the concatenated data to the output file.
    await fs.writeFile(outputPath, concatenatedData);
  } catch (error) {
    // Handle any errors that may occur during the process.
    console.error(error);
  }
}

// Retrieve input and output file paths from command line arguments.
const inputPathA = process.argv[2];
const inputPathB = process.argv[3];
const outputPath = process.argv[4];

// Call the function to concatenate files.
concatenateFiles(inputPathA, inputPathB, outputPath);
