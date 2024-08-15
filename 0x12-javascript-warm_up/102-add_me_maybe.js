#!/usr/bin/node

exports.addMeMaybe = function (number, cb) {
  if (typeof cb === 'function') {
    cb(number + 1);
  }
};
