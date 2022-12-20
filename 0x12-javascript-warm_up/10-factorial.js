#!/usr/bin/node

function factorial (FacNum) {
  if (FacNum === 0 || !Number(FacNum)) {
    return 1;
  } else {
    return FacNum * factorial(FacNum - 1);
  }
}
console.log(factorial(Number(process.argv[2])));
