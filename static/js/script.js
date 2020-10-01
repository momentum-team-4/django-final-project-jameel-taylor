let question
let answer

function checkAnswer(event) {
  if (event.target.value === answer) {
    event.target.classList.add('correct')
    event.target.classList.remove('incorrect')
  } else {
    event.target.classList.add('incorrect')
    event.target.classList.remove('correct')
  }
}



// #the random function used before, figure out how to change and use
// # function shuffle (cardsArray) {
//  #for (let i = cardsArray.length - 1; i > 0; i--) {
//     #const j = Math.floor(Math.random() * i)
//     #const temp = cardsArray[i]
//     #cardsArray[i] = cardsArray[j]
//     #cardsArray[j] = temp
//   #}
//   #return cardsArray
// #}
// #shuffle(cardsArray)
