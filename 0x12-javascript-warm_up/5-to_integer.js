#!/usr/bin/node

const argInt = parseInt(process.argv[2]);

if (process.argv[2] && argInt) {
  console.log('My number: ', argInt);
} else {
  console.log('Not a number');
}
