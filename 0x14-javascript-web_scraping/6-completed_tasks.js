#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) console.error(error);
  else {
    const resp = {};
    const arr = JSON.parse(body);
    arr.forEach((user) => {
      if (user.completed === true) {
        if (resp[user.userId] === undefined) {
          resp[user.userId] = 0;
        }
        resp[user.userId]++;
      }
    });
    console.log(resp);
  }
});
