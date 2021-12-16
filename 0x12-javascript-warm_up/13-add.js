#!/usr/bin/node
//  exports.add = (a, b) => a + b;
function notAdd (a, b) {
  return a + b;
}
exports.add = notAdd;
