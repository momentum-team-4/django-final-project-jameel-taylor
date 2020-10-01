const question
const answer

function checkAnswer(event) {

    if (event.target.value === answer) {
        event.target.classList.add('correct');
        event.target.classList.remove('incorrect');
    } else {
        event.target.classList.add('incorrect');
        event.target.classList.remove('correct');
    }
}