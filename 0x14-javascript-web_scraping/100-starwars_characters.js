#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request.get(url, (error, response, body) => {
  if (error) console.error(error);
  else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request.get(character, (errors, response, body) => {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
