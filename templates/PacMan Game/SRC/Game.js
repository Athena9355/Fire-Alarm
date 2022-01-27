
import TileMap from './TileMap.js';

/*define  canvas*/
const tileSize = 32;
const canvas = document.getElementById('gameCanvas'); /*get Canvas by ID*/
const ctx = canvas.getContext ('2d')/*get reference to the context of Canvas*/
const tileMap = new TileMap(tileSize); /*pass in tile size to tile map*/

function gameLoop(){ /*purpose: redraws the screen a certain number of times every second.*/
    tileMap.draw();
    /*next, we want to call the tilemap so that it draws the tile map*/
}

setInterval(gameLoop, 1000/75); /*calls a function every set period of time. calls 75 times every 1000 milisec*/