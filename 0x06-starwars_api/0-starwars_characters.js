#!/usr/bin/node

const request = require('request');
const args = process.argv;

if (args.length > 2) {
  const movieId = args[2];

  const baseUrl = 'https://swapi.dev/api/films/';

  const apiUrl = baseUrl + movieId + '/';

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error', error);
    } else if (response.statusCode !== 200) {
      console.error('Status code', response.statusCode);
    } else {
      const data = JSON.parse(body);
      const characterList = data.characters;

      async function fetchProcessCharacters () {
        for (const characterUrl of characterList) {
          try {
            const characterData = await fetchCharacter(characterUrl);
            console.log(characterData.name);
          } catch (err) {
            console.error('Error', err);
          }
        }
        // console.log('All characters processed');
      }

      async function fetchCharacter (characterUrl) {
        return new Promise((resolve, reject) => {
          request(characterUrl, (error, response, body) => {
            if (error) {
              console.error('Error', error);
              reject(error);
            } else if (response.statusCode !== 200) {
              console.error('Status code', response.statusCode);
              reject(new Error(`Failed to fetch character: ${characterUrl}`));
            } else {
              const characterData = JSON.parse(body);
              resolve(characterData);
            }
          });
        });
      }
      fetchProcessCharacters();
    }
  });
} else {
  console.log('Please provide id');
}
