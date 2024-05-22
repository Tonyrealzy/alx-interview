#!/usr/bin/node

const request = require("request");
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        } else {
          const characterData = JSON.parse(body);
          process.stdout.write(characterData.name + "\n");
        }
      });
    });
  }
});
