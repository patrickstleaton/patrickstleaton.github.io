//Play Again Button
var playAgain = document.querySelector("#b");
//Get all squares
var squares = document.querySelectorAll('td');

//Erase all squares
function clearBoard(){
  for (var i = 0; i < squares.length; i++){
    squares[i].textContent = '';
  }
}
playAgain.addEventListener('click', clearBoard);

//Check for X or O
function changeLetter(){
if(this.textContent === ''){
  this.textContent = 'O';
}else if(this.textContent === 'O'){
  this.textContent = 'X';
}else{
  this.textContent = '';
}
}

//Add event listener to squares
for (var i = 0; i<squares.length; i++){
  squares[i].addEventListener('click', changeLetter);
}
