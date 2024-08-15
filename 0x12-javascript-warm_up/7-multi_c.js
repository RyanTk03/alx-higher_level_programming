#!/usr/bin/node

const argInt = parseInt(process.argv[2]);

if (!argInt) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < argInt; i++) {
  console.log('C is fun');
}
