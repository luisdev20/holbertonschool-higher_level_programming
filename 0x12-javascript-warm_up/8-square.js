#!/usr/bin/node
const farg = Math.floor(Number(process.argv[2]));
if (isNaN(farg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < farg; i++) {
    console.log('x'.repeat(farg));
  }
}
