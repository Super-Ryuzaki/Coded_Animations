// Set up the canvas
var canvas = document.createElement("canvas");
document.body.appendChild(canvas);
var ctx = canvas.getContext("2d");

// Get the screen size
var screenWidth = window.innerWidth;
var screenHeight = window.innerHeight;

// Set the canvas size to match the screen size
canvas.width = screenWidth;
canvas.height = screenHeight;

// Define colors
var BLACK = "#000000";
var GREEN = "#00FF00";

// Create the raindrops
var raindrops = [];
for (var i = 0; i < 100; i++) {
  var x = Math.random() * screenWidth;
  var y = Math.random() * screenHeight;
  raindrops.push({ x: x, y: y });
}

// Main game loop
function gameLoop() {
  // Clear the canvas
  ctx.fillStyle = BLACK;
  ctx.fillRect(0, 0, screenWidth, screenHeight);

  // Update and draw the raindrops
  for (var i = 0; i < raindrops.length; i++) {
    // Move the raindrop down
    raindrops[i].y += 5;

    // Draw the raindrop as a text (0 or 1) in green color
    var text = Math.random() < 0.5 ? "0" : "1";
    ctx.font = "20px Arial";
    ctx.fillStyle = GREEN;
    ctx.fillText(text, raindrops[i].x, raindrops[i].y);

    // Reset the raindrop position when it reaches the bottom
    if (raindrops[i].y > screenHeight) {
      raindrops[i].y = Math.random() * -50 - 10;
      raindrops[i].x = Math.random() * screenWidth;
    }
  }

  // Request the next animation frame
  requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();
