#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newD = {};
for (user in dict) {
  if (dict[user] in newD) {
    newD[dict[user]].push(user);
  } else {
    newD[dict[user]] = [user];
  }
}
console.log(newD);
