#!/usr/bin/node
const { argv } = require('process');
if (!argv[2] | !argv[3]) {
  console.log(0);
  return;
}
new_arr = [];
for (let i =  0; i < argv.slice(2).length; i++) {
  new_arr.push(Number(argv.slice(2)[i]));
}
console.log(new_arr.sort(function(a, b){return a - b}).reverse()[1]);
