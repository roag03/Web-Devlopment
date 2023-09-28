let a=prompt("hey whats your age");

a=Number.parseInt(a);
console.log(typeof a)
if(a<0){
    alert("this is not a valid age");
}
else if(a<9){
 alert("you are a kid you cannot drive the car");
}
else if(a>9 && a<18){
 alert("you are a kid but you can drive the car after 18");
}
else if(a>18){
 alert("you are eligible to drive the car");
}
console.log("done")