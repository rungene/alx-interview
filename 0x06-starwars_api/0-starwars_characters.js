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
    }
    else if (response.statusCode !== 200) {
      console.error('Status code', response.statusCode);
    } 
    else {
      const data = JSON.parse(body);
      const characterList = data.characters

      const characterRequests = characterList.map(characterUrl => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (error, response, body) => {
            if (error) {
              console.error('Error', error);
              reject(error);
            }
            else if (response.statusCode !== 200) {
              console.error('Status code', response.statusCode);
              reject(new Error(`Failed to fetch character: ${characterURL}`));
            }
            else {
              const characterData = JSON.parse(body);
              console.log(characterData.name);
              resolve(characterData)
          }
          });
        });
      });
      // Wait all chracter request to complete
      Promise.all(characterRequests)
        .then(() => {
          console.log('All characters fetched successfully');
        })
        .catch(err => {
          console.error('Error:', err);
        });
      }
    });
} else {
  console.log('Please provide id');
}
