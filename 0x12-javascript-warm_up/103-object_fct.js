#!/usr/bin/node
/**
 * Define an object named 'myObject' with two properties:
 * - 'type': A string indicating the type of the object.
 * - 'value': A number representing the value of the object, initialized to 12.
 */
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/**
 * Add a method named 'incr' to 'myObject' that increments the 'value' property by 1.
 */
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
