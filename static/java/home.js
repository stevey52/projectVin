function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}


function setRandomColor() {
  $("#colorpad").css("background-color", getRandomColor());
}

var legen = document.querySelector("#vinnyHeader")

function ChangeHeaderColor(){
  colorInput = getRandomColor()
  legen.style.color = colorInput;
}

setInterval("ChangeHeaderColor()", 1000);

// adding an addEventListener on mouse hover to change textContent
var changeMidtext = document.querySelector("#midtext")
changeMidtext.addEventListener("mouseover",function(){
  changeMidtext.textContent = "Meet with the science of Light Balanced from indoor,outdoor and Black&White images";
  changeMidtext.style.color = "#008C8C";
})

// adding an addEventListener (mouseout)to reverse the change
changeMidtext.addEventListener("mouseout", function(){
  changeMidtext.textContent = "Indoor , outdoor to Black & white";
  changeMidtext.style.color = "black";
})
