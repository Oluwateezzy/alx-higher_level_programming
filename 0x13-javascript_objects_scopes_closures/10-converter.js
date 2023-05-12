#!/usr/bin/node

const converter =  (base) => {
  return (num) => {
    return num.toString(base);
  };
};
