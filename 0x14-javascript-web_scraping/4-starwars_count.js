#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) console.error(error);
  else {
    const films = JSON.parse(body).results;
    console.log(films.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
