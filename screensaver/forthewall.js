//I got this helpful code from the torus refrence.
let count = 0;
let cycle = 800;
let lastTarget = 0;
var x = 0;
var speed = 0.5;
//end of torus refrence

let snowflakes = []; //snowflakes example on this website
let detailY;

//i got this from the torus refrence
function setup() {
  createCanvas(400, 400, WEBGL);
  noStroke();
}
//end torus

function draw() {
  //background(0, 0, 0); //I got the rotate from the Torus refrence
  //Bianca helped me a bit with color functions so that I could have rainbow colors
  var Red =random(0, 250)
  var Green =random(0,250)
  var Blue =random(0, 250)
  var Alpha = (255)
  //end of rainbow colors
  
noStroke(); 
  //Here i was helped by the refrence for color, I took out the ellipse's and created dots that swirl around the screen!
c = color(100); 
fill(c); 
  
  noStroke();
  rotateX(frameCount * 0.02);  
  rotateY(frameCount * 2.5);  
  translate(100, 200)
  //torus(30, 15);
  //color functions with help from Bianca
  fill (Red, Green, Blue, Alpha);  
  let t = frameCount / 100;
  
  //this next section was a big help from the snowflake example, i played around with the numbers until i found what I wanted.
  for (let i = 0; i < random(8); i++) {   
    snowflakes.push(new snowflake()); 
  }
  for (let flake of snowflakes) {
    flake.update(t); 
    flake.display(); 
  }
  
  
  
  function snowflake() {
  this.posX = -40;
  this.posY = random(-60, 2);
  this.initialangle = random(30, 1 * PI);
  this.size = random(3, 5);

  this.radius = sqrt(random(pow(width / 2, 2)));

  this.update = function(time) {
    let w = 0.9; 
    let angle = w * time + this.initialangle;
    this.posX = width / 2 + this.radius * sin(angle);

    this.posY += pow(this.size, 0.8);

    if (this.posY > height) {
      let index = snowflakes.indexOf(this);
      snowflakes.splice(index, 1);
    }
  };

  this.display = function() {
    ellipse(this.posX, this.posY, this.size);
  };
}
  
  }
{
  x =x + speed;
  //x=x +3;
}

//end snowflake example help
