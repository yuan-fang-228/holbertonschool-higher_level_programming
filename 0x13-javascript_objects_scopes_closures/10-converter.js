#!/usr/bin/node
exports.converter = function (base) {
  return function converNum (n) {
    return (n.toString(base));
  };
};
