#!/usr/bin/node

const esrever = (list) => {
  const rev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return (rev);
};
module.exports = { esrever };
