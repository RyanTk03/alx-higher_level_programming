#!/usr/bin/node

const argInt = parseInt(process.argv[1]);

if (!argInt) {
  console.log('Missing size');
}
for (let i = 0; i < argInt; i++) {
  console.log('X'.repeat(argInt));
}
