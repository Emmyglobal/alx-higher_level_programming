#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  const temp = list.length - 1;
  for (let i = temp; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return (reversedList);
};
