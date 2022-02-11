let randomNum;

setInterval(function(){
    randomNum = window.Math.floor(Math.random(0, 1000)* 1000);
}, 10000);


export { randomNum };
