// 5 get the median out of 5 doubles


2 > 0 > 2

const num1 = 140;
const num2 = -101;
const num3 = 53;
const num4 = 12;
const num5 = -5;
let counter = 0;

const stuff = (num1, num2, num3, num4, num5) => {
  const count = (num1, num2) => {
    if (num1 > num2) {
      counter++;
    } else {
      counter--;
    }
  };

  count(num1, num2);
  count(num1, num3); 
  count(num1, num4);
  count(num1, num5);

  if (counter == 0) {
    console.log(num1);
  };

  counter = 0;
}

stuff(num1, num2, num3, num4, num5);
stuff(num2, num1, num3, num4, num5);
stuff(num3, num2, num1, num4, num5);
stuff(num4, num2, num3, num1, num5);
stuff(num5, num2, num3, num4, num1);

let array = [num1, num2, num3, num4, num5]
array.sort()
console.log(Math.floor(array.length() / 2))