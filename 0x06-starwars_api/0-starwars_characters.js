#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;
  
      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            const characterData = JSON.parse(body);
            process.stdout.write(characterData.name + '\n');
          }
        });
      });
    }
  });