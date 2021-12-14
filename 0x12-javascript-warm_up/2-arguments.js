#!/usr/bin/env node
const args = process.argv;
console.log(args.length === 2 ? 'No argument' : args.length === 3 ? 'Argument found' : 'Arguments found');
