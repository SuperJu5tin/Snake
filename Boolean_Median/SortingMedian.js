// 5 get the median out of 5 doubles


2 > 0 > 2

const num1 = 10;
const num2 = -10;
const num3 = 5;
const num4 = 0;
const num5 = -5;
let counter = 0;

const stuff = (num1, num2, num3, num4, num5) => {
  console.log
  const count = () => {
    if (num1 > num2) {
      counter++;
    } else {
      counter--;
    }
    console.log(num1, counter)
  };

  count(num1, num2);
  count(num1, num3); 
  count(num1, num4);
  count(num1, num5);

  if (counter == 3) {
    console.log(num1);
  };

  counter = 0;
}

stuff(num1, num2, num3, num4, num5);
stuff(num2, num1, num3, num4, num5);
stuff(num3, num2, num1, num4, num5);
stuff(num4, num2, num3, num1, num5);
stuff(num5, num2, num3, num4, num1);