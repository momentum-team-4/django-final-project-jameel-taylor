const Front
const Back

function checkAnswer(event) {
    /*
        Check whether the 
    */

    if (event.target.value === Back) {
        event.target.classList.add('correct');
        event.target.classList.remove('incorrect');
    } else {
        event.target.classList.add('incorrect');
        event.target.classList.remove('correct');
    }
}