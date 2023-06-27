import { Column } from "./column.js";

const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const FONT_SIZE = 16;

context.font = 'bold 16px monospace';

const columns = [];
const columnsCount = canvas.width / FONT_SIZE; 

for (let i = 0; i < columnsCount; i++){
    columns.push(new Column(i * FONT_SIZE, FONT_SIZE , canvas.height, context));
}

const column = new Column(100, FONT_SIZE , canvas.height, context);

function animate() {

    context.fillStyle = "rgba(0, 0, 0, 0.05)";
    context.fillRect(0, 0, canvas.width, canvas.height);
    
    context.fillStyle = "rgb(0, 141, 78)";
    columns.forEach(column => column.drawSymbol()); 
    column.drawSymbol();
     
    setTimeout(() => requestAnimationFrame(animate), 50);
}

animate();
