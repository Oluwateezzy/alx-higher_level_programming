#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    print(characters, 0);
  }
});

function print (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        print(characters, index + 1);
      }
    }
  });
}
