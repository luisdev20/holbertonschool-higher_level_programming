#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return 'NaN';
  } else {
    return (a + b);
  }
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
