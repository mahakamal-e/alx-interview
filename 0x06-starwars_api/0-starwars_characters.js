#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Define the API URL with the provided movieId
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the film data
request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error(`Failed to fetch film data. Status code: ${res.statusCode}`);
    return;
  }

  const characters = body.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  // Function to fetch each character's data
  const fetchCharacterName = (url, callback) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        callback(err);
        return;
      }

      if (res.statusCode !== 200) {
        callback(`Failed to fetch character data. Status code: ${res.statusCode}`);
        return;
      }

      callback(null, body.name);
    });
  };

  // Function to print all character names
  const printCharacterNames = (urls) => {
    let remaining = urls.length;

    urls.forEach((url) => {
      fetchCharacterName(url, (err, name) => {
        if (err) {
          console.error(err);
          return;
        }

        console.log(name);
        remaining--;

        if (remaining === 0) {
          process.exit();
        }
      });
    });
  };

  printCharacterNames(characters);
});
