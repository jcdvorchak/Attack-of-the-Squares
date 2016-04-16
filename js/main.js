/**
 * Attack of the Squares
 * Joey Dvorchak
 */


var game = new Phaser.Game(window.innerWidth, window.innerHeight, Phaser.CANVAS, '', { preload: preload, create: create, update: update });

// load any assets
function preload() {

}

var scaleRatio = window.devicePixelRatio;

var squareGroup;
var circleGroup;
var bulletGroup;
var bullet;

var score = 0;
var scoreText;

var cursors;

var width;
var height;
var shapeWidth;

var bulletSpeed = 200;
var squareSpeed = -200;
var squarePixelDelay = 50;

// prep everything, one time run
function create() {
    width = game.world.width/scaleRatio;
    height = game.world.height/scaleRatio;

    game.physics.startSystem(Phaser.Physics.ARCADE);

    // game.add.sprite(0,0,'background');

    squareGroup = game.add.group();
    squareGroup.enableBody = true;
    circleGroup = game.add.group();
    circleGroup.enableBody = true;
    bulletGroup = game.add.group();
    bulletGroup.enableBody = true;

    var xRatio = height/5;
    shapeWidth = width/16;
    var drawnObject;
    for (var i = 1; i < 5; i+=1) {
       
        // circleGroup
        bmd = game.add.bitmapData(shapeWidth,shapeWidth);
        bmd.ctx.beginPath();
        bmd.circle(shapeWidth/2, shapeWidth/2, (shapeWidth/2)-1, 'rgb(0,102, 255)');
        drawnObject = game.add.sprite(width/14, xRatio*i, bmd);
        circleGroup.add(drawnObject);
        drawnObject.anchor.setTo(0.5);
        drawnObject.body.immovable = true;
        drawnObject.inputEnabled = true;
        
        drawnObject.events.onInputOver.add(circleOver, this);
        drawnObject.events.onInputOut.add(circleOut, this);


        // squareGroup
        var bmd = game.add.bitmapData(shapeWidth,shapeWidth);
        bmd.ctx.beginPath();
        bmd.ctx.rect(0, 0, shapeWidth, shapeWidth);
        bmd.ctx.fillStyle = '#FF0000';
        bmd.ctx.fill();
        drawnObject = game.add.sprite(width-(width/14), xRatio*i, bmd);
        squareGroup.add(drawnObject);
        drawnObject.anchor.setTo(0.5);
        drawnObject.body.velocity.x = squareSpeed;
    }

    // bullet
    var bmd = game.add.bitmapData(shapeWidth*(3/4),shapeWidth/3);
    bmd.ctx.beginPath();
    bmd.ctx.rect(0, 0, shapeWidth*(3/4), shapeWidth/3);
    bmd.ctx.fillStyle = '#FFFF00';
    bmd.ctx.fill();
    drawnObject = game.add.sprite(-100, xRatio, bmd); // start offscreen
    bulletGroup.add(drawnObject);
    drawnObject.anchor.setTo(0.5);
    drawnObject.collideWorldBounds=true;

    bullet = drawnObject;

    scoreText = game.add.text(16, 16, 'score: '+score, { fontSize: '32px', fill: '#900' });
}

// game updates every .. frame?
function update() {
    game.physics.arcade.collide(squareGroup, bulletGroup, bulletSquareCollision, null, this);
    game.physics.arcade.collide(squareGroup, circleGroup, circleSquareCollision, null, this);
}

// called on mouse over of a circle
function circleOver(circle, bullet) {
    resetBullet(circle.y);
}

// called on mouse out of a circle
function circleOut() {
    stopBullet();
}

// called when bullets and squares collide
function bulletSquareCollision(square, bullet) {
    score++;
    updateScore();

    resetBullet();
    resetSquare(square);
}

// called when circles and squares collide
function circleSquareCollision(square, circle) {
    score-=5;
    updateScore();

    resetSquare(square);
}

// reset to the bullet in front of the circle
// circle is determined with the height parameter
// if height is not passed the bullet stays in the same row
function resetBullet(height) {
    bullet.x = (width/14)+(shapeWidth*3/4);
    bullet.body.velocity.x = bulletSpeed;

    if (height != null) {
        bullet.y = height;
    }
}

// move the bullet offscreen to simulate it dissapearing
function stopBullet() {
    bullet.x = -100;
    bullet.body.velocity.x = 0;
}

// reset the square to a (mostly) random point beyond the left margin
function resetSquare(square) {
    square.x = width+(getRandomInt(0,10)*squarePixelDelay);
    square.body.velocity.x = squareSpeed;
}



// update the score text
function updateScore() {
    scoreText.text = 'score: ' + score;
}

// returns a random integer between min and max
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}