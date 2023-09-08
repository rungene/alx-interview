#!/usr/bin/node

const request = require('request');
const args = process.argv;

if (args.length > 2) {
  const movieId = args[2];

  const baseUrl = 'https://swapi.dev/api/people/';

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

      console.log('Name', data.name);
      console.log('Height', data.height);
    }
  });
} else {
  console.log('Please provide id');
}
