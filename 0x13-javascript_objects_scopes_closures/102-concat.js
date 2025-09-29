#!/usr/bin/node
/* script that concats 2 files */

const fs = require('fs');
const args = process.argv.slice(2);

const fileA = args[0];
const fileB = args[1];
const fileC = args[2];

const dataA = fs.readFileSync(fileA, 'utf8');
const dataB = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(fileC, dataA + dataB);
