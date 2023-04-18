#!/usr/bin/node
const { argv } = require('process');
if (!argv[2] | !argv[3]) {
  console.log(0);
  return;
}
console.log(argv.slice(2).sort().reverse()[1]);
