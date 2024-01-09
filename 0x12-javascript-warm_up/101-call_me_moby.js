#!i/usr/bin/node
/* function that executes x times a function. */

function callMeMoby (x, Func) {
  for (let i = 0; i < x; i++) {
    Func();
  }
}

module.exports.callMeMoby = callMeMoby;
