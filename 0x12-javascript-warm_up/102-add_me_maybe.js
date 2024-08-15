#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  if (typeof theFunction === 'function') {
    theFunction(number + 1);
  }
};
