// 5 get the median out of 5 doubles

// array of numbers

const num1 = Math.random() < .5 ? Math.random() * -100 : Math.random() * 100;
const num2 = Math.random() < .5 ? Math.random() * -100 : Math.random() * 100;
const num3 = Math.random() < .5 ? Math.random() * -100 : Math.random() * 100;
const num4 = Math.random() < .5 ? Math.random() * -100 : Math.random() * 100;
const num5 = Math.random() < .5 ? Math.random() * -100 : Math.random() * 100;
let counter = 0;

// ez mode with array

let array = [num1, num2, num3, num4, num5]
array.sort()
for (let i = 0; i < array.length; i++) {
  console.log(`Number ${i + 1} ` + array[i]);
}
console.log(array[Math.floor(array.length / 2)])

// hardmode with if statements

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