/**
 * Attack of the squareGroup
 * Joey Dvorchak
 */

/**
 * TODO
   - auto sizing / ratio
    - window.screen.width/height
 *
 */

// scaling a sprite also scalse the x and y :(
// boundaries are still the same ^^ for collision

var game = new Phaser.Game(window.innerWidth, window.innerHeight, Phaser.CANVAS, '', { preload: preload, create: create, update: update });

function preload() {

    game.load.image('background', 'assets/background.png');
    // game.load.image('square', 'assets/square.png');
    // game.load.image('circle', 'assets/circle.png');
    // game.load.image('bullet', 'assets/bullet.png');


}

var scaleRatio = window.devicePixelRatio;
// game.world._container.scale.set(scaleRatio,scaleRatio)

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
    drawnObject = game.add.sprite(width/14+(shapeWidth*(3/4)), xRatio, bmd);
    bulletGroup.add(drawnObject);
    drawnObject.anchor.setTo(0.5);
    drawnObject.body.velocity.x = bulletSpeed;
    drawnObject.collideWorldBounds=true;

    bullet = drawnObject;

    //  The score
    scoreText = game.add.text(16, 16, 'score: '+score, { fontSize: '32px', fill: '#900' });

    //  Our controls.
    // cursors = game.input.keyboard.createCursorKeys();
}

function update() {
    game.physics.arcade.collide(squareGroup, bulletGroup, bulletSquareCollision, null, this);
    game.physics.arcade.collide(squareGroup, circleGroup, circleSquareCollision, null, this);
}


function circleOver(circle, bullet) {
    resetBullet(circle.y);
}

function circleOut() {
    // stopBullet();
}


function bulletSquareCollision(square, bullet) {
    score++;
    updateScore();

    resetBullet();
    resetSquare(square);
}

function circleSquareCollision(square, circle) {
    score-=5;
    updateScore();

    resetSquare(square);
}


function resetBullet(height) {
    bullet.x = (width/14)+(shapeWidth*3/4);
    bullet.body.velocity.x = bulletSpeed;

    if (height != null) {
        bullet.y = height;
    }
}

function stopBullet() {
    resetBullet();
    bullet.body.velocity.x = 0;
}

function resetSquare(square) {
    square.x = width+(getRandomInt(0,4)*squarePixelDelay);
    square.body.velocity.x = squareSpeed;
}



// update the score text
function updateScore() {
    scoreText.text = 'score: ' + score;
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}