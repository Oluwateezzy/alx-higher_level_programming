#!/usr/bin/node
const { argv } =  require("process");

function fact (a) {
  if (Number(a) === 'NaN') return Number(a);
  if (a >= 1) return a * fact(a - 1);
  else return 1;
}
console.log(fact(argv[2]));
