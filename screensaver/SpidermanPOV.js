let count = 0;
let cycle = 800;
let lastTarget = 0;
var x = 0;
var speed = 1;
let snowflakes = []; //snowflakes example on this website
let detailY;


function setup() {
  createCanvas(1920, 1080, WEBGL); 
  noStroke();
  background(0, 0, 0); //I got the rotate from the Torus refrence
}

function draw() {
  //i took the background and put it in setup instead to fix some issues
  var Red =random(0, 250)
  var Green =random(0,250)
  var Blue =random(0, 250)
  var Alpha = (255)
  
noStroke(); 
  //Here i was helped by the refrence for color, I took out the ellipse's and created dots that swirl around the screen!
c = color(100); 
fill(c); 
  
  noStroke();
  rotateX(frameCount * 0.02);  //0.01 for slow or 0.02
  rotateY(frameCount * 2.5);  //what!  0.01 or 0.03 2.5 if you feel lucky
  translate(100, 200)
  //torus(30, 15);
  //color functions with help from Bianca
  fill (Red, Green, Blue, Alpha);  //color1, color2, color3);
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
