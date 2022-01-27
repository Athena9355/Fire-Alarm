export default class TileMap{
    constructor(tileSize){ /*defined how big ecah tile will be*/
        this.tileSize = tileSize;
    }
//this array will represent the entire array. and in the array, we will have rows. i.e. have arrays of arrays
    //we will assign numbers to items. brick = 1, pallet = 0
    map = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1],//bc the first row will be all bricks, it will all be 1
        [1,0,0,0,0,0,0,0,0,0,0,0,1], //1 brick on both ends
        [1,0,0,0,0,0,0,0,0,0,0,0,1], //1 brick on both ends
        [1,0,0,0,0,0,0,0,0,0,0,0,1], //1 brick on both ends
        [1,0,0,0,0,0,0,0,0,0,0,0,1], //1 brick on both ends
        [1,0,0,0,0,0,0,0,0,0,0,0,1], //1 brick on both ends
        [1,0,0,0,0,0,0,0,0,0,0,0,1], //1 brick on both ends
        [1,0,0,0,0,0,0,0,0,0,0,0,1], //1 brick on both ends
        [1,0,0,0,0,0,0,0,0,0,0,0,1], //1 brick on both ends
        [1,1,1,1,1,1,1,1,1,1,1,1,1],
    ];

    draw(){
        //console.log("draw"); /*defined a method called draw*/
    }
}
/*since we exported here, we will inport it in game*/