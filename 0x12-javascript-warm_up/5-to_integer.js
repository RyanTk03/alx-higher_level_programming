#!/usr/bin/node

const argInt = parseInt(process.argv[1]);

if (process.argv[1] && argInt) {
  console.log('My number: ', argInt);
} else {
  console.log('Not a number');
}
