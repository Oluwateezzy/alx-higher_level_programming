#!/usr/bin/node
const { argv } = require('process');

if (argv[2]) {
  if (Number(argv[2]) !== 'NaN') {
    for (let i = 0; i < Number(argv[2]); i++) console.log('C is fun');
  }
} else console.log('Missing number of occurrences');
