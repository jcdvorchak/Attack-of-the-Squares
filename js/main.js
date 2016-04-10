/**
 * Attack of the Squares
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
    game.load.image('square', 'assets/square.png');
    game.load.image('circle', 'assets/circle.png');
    game.load.image('bullet', 'assets/bullet.png');


}

var scaleRatio = window.devicePixelRatio / 3;
// game.world._container.scale.set(scaleRatio,scaleRatio)

var squares;
var circles;
var bullets;

var score = 0;
var scoreText;

var cursors;

var width;
var height;

function create() {
    width = game.world.width/scaleRatio;
    height = game.world.height/scaleRatio;

    game.physics.startSystem(Phaser.Physics.ARCADE);

    game.add.sprite(0,0,'background');

    squares = game.add.group();
    squares.enableBody = true;
    circles = game.add.group();
    circles.enableBody = true;
    bullets = game.add.group();
    bullets.enableBody = true;


    // create circles, squares, bullets
    circles.scale.setTo(scaleRatio,scaleRatio);
    squares.scale.setTo(scaleRatio,scaleRatio);
    bullets.scale.setTo(scaleRatio,scaleRatio);
    for (var i = 1; i < 10; i+=2) 
    {
        var circle = circles.create((width/14), ((height/8)*(i)), 'circle');
        circle.anchor.setTo(0.5);
        circle.body.immovable = true;

        var square = squares.create((width/2), ((height/8)*(i)), 'square');
        square.anchor.setTo(0.5);

        var bullet = bullets.create((width), ((height/8)*(i)), 'bullet');
        bullet.anchor.setTo(0.5);

        bullet.body.gravity.x = -300;
        // bullet.body.gravity.y = 0;
        // bullet.body.collideWorldBounds=true; // breaks cause ratio crap
    }


    //  The score
    // scoreText = game.add.text(16, 16, 'score: 0', { fontSize: '32px', fill: '#900' });

    //  Our controls.
    // cursors = game.input.keyboard.createCursorKeys();
}

function update() {
    game.physics.arcade.collide(circles, bullets, resetBullet, null, this);
}



function resetBullet(circle, bullet) {
    bullet.x = (width);
}