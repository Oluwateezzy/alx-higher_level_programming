#!/usr/bin/node

let count = 0;

const logMe = (item) => {
  console.log(`${count}: ${item}`);
  count++;
};

module.exports = { logMe };
