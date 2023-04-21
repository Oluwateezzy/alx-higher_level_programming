#!/usr/bin/node
const { argv } = require('process');
if (!argv[2] | !argv[3]) {
  console.log(0);
} else {
  const newArr = [];
  for (let i = 0; i < argv.slice(2).length; i++) {
    newArr.push(Number(argv.slice(2)[i]));
  }
  console.log(newArr.sort(function (a, b) { return a - b; }).reverse()[1]);
}
