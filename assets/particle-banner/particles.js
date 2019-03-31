// Kass's Customizable Node/Particles Title

// settings:
const canvasName = "did-canvas"
const maxNodes = 100 // using too many will impact performance.
const nodeMinSize = 2 
const nodeMaxSize = 4
const nodeMinSpeed = 0.03
const nodeMaxSpeed = 0.8
const nodeMaxConnections = 20
const connectionThickness = 1 
const connectionDist = 100
const connectionColor = "#ffffff"
const nodeColors = ["#ff9900", "ffcc99"] // you may enter multiple colors
const warpEdges = false // if false nodes will bounce off the edges
const useIcon = false // if false then colored circles will be used
const iconPath = "https://image.flaticon.com/icons/png/128/137/137068.png"
const iconScale = 6
const useTrail  = false
const backgroundColor = "#222222"
// another example can be found here https://codepen.io/cryptokass/pen/mgbajy?editors=0010

// canvas reference:
var canvas = document.getElementById(canvasName)
var ctx = canvas.getContext('2d')

// store canvas size:
let canvasHeight = +getComputedStyle(canvas).getPropertyValue("height").slice(0, -2);
let canvasWidth = +getComputedStyle(canvas).getPropertyValue("width").slice(0, -2);

canvas.height = canvasHeight
canvas.width = canvasWidth

// setup image
var img = new Image()
img.src = iconPath

// animation frame compatibility:
window.requestAnimFrame = function()
	{
		return (
			window.requestAnimationFrame       || 
			window.webkitRequestAnimationFrame || 
			window.mozRequestAnimationFrame    || 
			window.oRequestAnimationFrame      || 
			window.msRequestAnimationFrame     || 
			function(callback) { window.setTimeout(callback, 1000 / 60) }
		);
}();

// node class
function Node(){
  
  this.size = nodeMinSize + Math.random() * (nodeMaxSize-nodeMinSize)
  this.x = canvasWidth * Math.random()
  this.y = canvasHeight * Math.random()
  this.color = nodeColors[Math.floor(Math.random()*nodeColors.length)]
  this.connections = 0
  
  // calculate starting velocity
  let speed = nodeMinSpeed + Math.random() * (nodeMaxSpeed-nodeMinSpeed)
  let theta = Math.random() * Math.PI * 2
  this.velocity = {x:speed * Math.sin(theta), y:speed * Math.cos(theta)}
  
  // move this node
  this.move = function(){
    if (this.x + this.velocity.x >= canvas.width || this.x + this.velocity.x <= 0){
      if (warpEdges){
        this.x = (this.x + this.velocity.x >= canvas.width ) ? 0 : canvas.width
      } else {
        this.velocity.x = -this.velocity.x
      }
    }
    if (this.y + this.velocity.y >= canvas.height || this.y + this.velocity.y <= 0)
      {
        if (warpEdges) {
          this.y = (this.y + this.velocity.y >= canvas.height ) ? 0 : canvas.height
        } else {
          this.velocity.y = -this.velocity.y
        }
        
      }
    this.x += this.velocity.x
    this.y += this.velocity.y
    this.connections = 0
  }
  
  // draw this nodes connections
  this.drawConnections = function(index){
    for (let i=index+1; i < nodes.length; i++){
      let node = nodes[i]
      let dist = Math.sqrt(Math.pow(this.x - node.x,2) + Math.pow(this.y - node.y,2))
      
      if (dist < connectionDist && node.connections < nodeMaxConnections && this.connections < nodeMaxConnections){
        ctx.globalAlpha = 1-dist/connectionDist
        ctx.beginPath()
        ctx.moveTo(this.x,this.y)
        ctx.lineTo(node.x, node.y)
        ctx.lineWidth = connectionThickness
        ctx.strokeStyle = connectionColor
        ctx.stroke()
        ctx.closePath()
        node.connections++
        this.connections++
      }
    }
  }
  
  this.draw = function(){
    ctx.globalAlpha = 1
    if (useIcon){
      let _size = this.size * iconScale
      let dx = this.x - _size/2
      let dy = this.y - _size/2
      ctx.drawImage(img, dx, dy, _size, _size)
    }else{
      ctx.beginPath()
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2)
      ctx.fillStyle = this.color
      ctx.fill()
      ctx.closePath()
    }
  }
}

var nodes = []
for (let i=0; i < maxNodes; i++){
  var node = new Node()
  nodes.push(node)
}

function tick(){
  if (useTrail){
    ctx.globalAlpha = 0.1
    ctx.rect(0,0,canvas.width, canvas.height)
    ctx.fillStyle = backgroundColor
    ctx.fill()
  }else{
   ctx.clearRect(0, 0, canvas.width, canvas.height)
  }
  for (let i=0; i < maxNodes; i++){
    nodes[i].drawConnections(i)
  }
  for (let i=0; i < maxNodes; i++){
    nodes[i].draw()
    nodes[i].move()
  }
  requestAnimFrame(tick);
}

requestAnimFrame(tick);