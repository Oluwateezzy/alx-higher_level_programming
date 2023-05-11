#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
  let i;
  for (i = 0; i < x; i++) theFunction();
};
