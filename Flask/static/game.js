let score = 0, timeLeft = 60, timerId, currentAnswer;

function startGame() {
    score = 0; timeLeft = 60;
    document.getElementById("start-screen").style.display = "none";
    document.getElementById("result-screen").style.display = "none";
    document.getElementById("game-screen").style.display = "block";
    document.getElementById("score").innerText = score;
    document.getElementById("timer").innerText = timeLeft;
    generateProblem();
    timerId = setInterval(countdown, 1000);
}

function countdown() {
    timeLeft--;
    document.getElementById("timer").innerText = timeLeft;
    if (timeLeft <= 0) endGame();
}

function generateProblem() {
    let a = Math.floor(Math.random() * 10);
    let b = Math.floor(Math.random() * 10);
    if (Math.random() > 0.5) {
        currentAnswer = a + b;
        document.getElementById("problem").innerText = `${a} + ${b}`;
    } else {
        currentAnswer = a - b;
        document.getElementById("problem").innerText = `${a} - ${b}`;
    }
}

function submitAnswer() {
    let ans = parseInt(document.getElementById("answer").value);
    if (ans === currentAnswer) {
        score++;
        document.getElementById("score").innerText = score;
    }
    document.getElementById("answer").value = "";
    generateProblem();
}

function endGame() {
    clearInterval(timerId);
    document.getElementById("game-screen").style.display = "none";
    document.getElementById("result-screen").style.display = "block";
    document.getElementById("finalScore").innerText = score;

    let high = localStorage.getItem("highscore") || 0;
    if (score > high) {
        localStorage.setItem("highscore", score);
        high = score;
    }
    document.getElementById("finalHighscore").innerText = high;
    document.getElementById("highscore").innerText = "High Score: " + high;
}
