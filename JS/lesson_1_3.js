"use strict"
let result = 10 + 10 + "10";
console.log(result); // 10+10 = 20 -> "20" + "10" = 2010 было произведено приведение
 
 let result = 10 + "10" + 10;
 console.log(result); // "10" + "10" + "10" = 101010 так же было произведено приведение

let result = 10 + 10 + +"10";
console.log(result); // 10+10-> 20 + 10 = 30 приведение строки "10" к числу при помощи унарного плюса

let result = 10 / -""; // 10 / -0 -> получаем -Infinity бесконечность
console.log(result);

let result = 10 / +"2,5"; // 10 / NaN = NaN. Из-за запятой приведение происходит неккоректно
console.log(result);