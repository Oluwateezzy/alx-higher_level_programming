#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) console.error(error);
  else {
    const films = JSON.parse(body).results;
    let count = 0;
    console.log(films.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1 : count;
    }, 0));
  }
});
