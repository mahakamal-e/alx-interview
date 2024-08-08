#!/usr/bin/node
const rp = require('request-promise');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Define the API URL with the provided movieId
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch character data
const fetchCharacterName = async (url) => {
  try {
    const character = await rp({ uri: url, json: true });
    return character.name;
  } catch (error) {
    console.error(`Failed to fetch character data from ${url}: ${error.message}`);
    return null;
  }
};

// Main function to fetch movie data and character names
const fetchMovieAndPrintCharacters = async () => {
  try {
    // Fetch movie data
    const movie = await rp({ uri: apiUrl, json: true });
    const characterUrls = movie.characters;

    if (!characterUrls || characterUrls.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    // Fetch and print all character names
    for (const url of characterUrls) {
      const name = await fetchCharacterName(url);
      if (name) {
        console.log(name);
      }
    }
  } catch (error) {
    console.error(`Failed to fetch movie data: ${error.message}`);
  }
};

fetchMovieAndPrintCharacters();
