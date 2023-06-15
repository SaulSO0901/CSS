//Ejercicio 1
/*var score=8;
console.log("Mid leveled skils",score>0 && score<10);*/
////////////////////////////////////////////////////////////

//Ejercicio 2 
/*
var timeRemaining=0,energy=10;
console.log("Game over: ",timeRemaining == 0 || energy == 0);*/
////////////////////////////////////////////////////////////

//Ejercicio 3
/*
var n1=2,n2=5;
var odd;
console.log("Is"+n1+" an odd number?",n1%2==0);
console.log("Is"+n2+" an odd number?",n2%2==0);*/
////////////////////////////////////////////////////////////

//Ejercicio 4
/*
var counter = 0;
counter += 5;
counter += 3;
console.log(counter); */ 
/*
for (var i = 1; i <= 10; i++) {
    if(i == 1) {
        console.log("Gold medal")
    } else if (i == 2) {
        console.log("Silver medal")
    } else if (i == 3) {
        console.log("Bronze medal")
    } else {
        //this block will run if no condition matches
        console.log(i)
    }
}
*/

/*
for (var i = 1; i <= 10; i++) {
    switch(i) {
        case 1:
            console.log("Gold medal")
            break
        case 2:
            console.log("Silver medal")
            break
        case 3:
            console.log("Bronze medal")
            break
        default:
            //this block will run if no condition matches
            console.log(i)
    }
}
*/

 
/*Math .random
Math.random();

var decimal= Math.random();

console.log(decimal);

console.log(decimal*10);*/

/*math que redondea
var rounded= Math.ceil(.0001);

console.log(rounded);*/

/*Cadenas como arrays
var greeting="howdy";
var greet=["Hello","Bye","Sayonara"];
for(var i=0;i< greeting.length;i++){
console.log(greeting[i]);


}

for(var i=0;i< greet.length;i++){
    console.log(greet[i]);
    
    
    }
*/

var greet='hello';
var user = 'lisa';

//console.log(greet.pop());

console.log(greet+' '+user);

console.log(greet.concat(user));

//arrays

var clothes = [];
clothes.push('gray t-shirt'); // 1st item of clothing
clothes.push('blue t-shirt'); // 2nd item of clothing
clothes.push('yellow t-shirt'); // 3rd item of clothing
clothes.push('slippers'); // 4th item of clothing
clothes.push('old jeans'); // 5th item of clothing
clothes.pop();
clothes.push('green scarf');
console.log(clothes[2]);

