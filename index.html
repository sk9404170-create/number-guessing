<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Number Guessing Game</title>
<style>
  :root {
    --bg: #0f172a;
    --card: #1e293b;
    --box: #334155;
    --muted: #94a3b8;
    --muted2: #64748b;
    --text: #e2e8f0;
    --blue: #38bdf8;
    --green: #22c55e;
    --yellow: #facc15;
    --amber: #f59e0b;
    --red: #ef4444;
    --purple: #7c3aed;
    --purple2: #c084fc;
  }

  * { box-sizing: border-box; }

  html, body {
    margin: 0;
    padding: 0;
    background: var(--bg);
    color: var(--text);
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    height: 100%;
    overflow-x: hidden;
  }

  .main {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    padding: 30px 16px 20px;
  }

  h1.title {
    font-size: 34px;
    font-weight: 700;
    color: var(--blue);
    margin: 10px 0 5px;
    text-align: center;
  }

  .subtitle {
    font-size: 13px;
    color: var(--muted);
    margin: 0 0 20px;
    text-align: center;
  }

  .difficulty-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
  }

  .difficulty-row label {
    font-size: 12px;
    font-weight: 700;
    color: #cbd5e1;
  }

  select#difficulty {
    background: var(--box);
    color: white;
    font-family: inherit;
    font-size: 11px;
    font-weight: 700;
    border: none;
    border-radius: 4px;
    padding: 8px 10px;
    width: 130px;
    cursor: pointer;
  }

  .card {
    background: var(--card);
    width: 680px;
    max-width: 92vw;
    min-height: 610px;
    border-radius: 6px;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 30px 24px;
  }

  .range-label {
    font-size: 16px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 20px;
    text-align: center;
  }

  .stats {
    display: flex;
    gap: 8px;
    margin-bottom: 25px;
    flex-wrap: wrap;
    justify-content: center;
  }

  .stat-box {
    background: var(--box);
    width: 160px;
    height: 80px;
    border-radius: 4px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
  }

  .stat-title {
    font-size: 9px;
    font-weight: 700;
    color: var(--muted);
    letter-spacing: 0.5px;
  }

  .stat-value {
    font-size: 17px;
    font-weight: 700;
  }

  #attemptValue { color: var(--blue); }
  #timeValue { color: var(--green); }
  #scoreValue { color: var(--yellow); }

  .progress-track {
    width: 530px;
    max-width: 100%;
    height: 14px;
    background: var(--box);
    border-radius: 2px;
    margin-bottom: 25px;
    overflow: hidden;
  }

  .progress-fill {
    height: 100%;
    width: 0%;
    background: var(--blue);
    transition: width 0.25s ease;
  }

  .input-label {
    font-size: 10px;
    font-weight: 700;
    color: var(--muted);
    letter-spacing: 0.5px;
    margin-bottom: 12px;
  }

  input#guessInput {
    background: var(--bg);
    color: white;
    border: none;
    border-radius: 4px;
    font-family: inherit;
    font-size: 24px;
    font-weight: 700;
    text-align: center;
    width: 220px;
    padding: 14px 0;
    margin-bottom: 12px;
    outline: none;
  }

  input#guessInput:disabled {
    opacity: 0.5;
  }

  .buttons {
    display: flex;
    gap: 6px;
    margin-bottom: 20px;
    flex-wrap: wrap;
    justify-content: center;
  }

  button {
    font-family: inherit;
    font-size: 12px;
    font-weight: 700;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    padding: 14px 0;
    width: 190px;
    color: white;
  }

  button:disabled {
    cursor: not-allowed;
    opacity: 0.5;
  }

  #guessBtn { background: #0284c7; }
  #guessBtn:hover:not(:disabled) { background: #0369a1; }

  #hintBtn { background: var(--purple); }
  #hintBtn:hover:not(:disabled) { background: #6d28d9; }

  #newGameBtn {
    background: #475569;
    width: 420px;
    max-width: 100%;
    padding: 15px 0;
    margin-top: 4px;
  }
  #newGameBtn:hover { background: #64748b; }

  .result-label {
    font-size: 13px;
    font-weight: 700;
    color: white;
    text-align: center;
    max-width: 500px;
    min-height: 50px;
    white-space: pre-line;
    margin-bottom: 16px;
    line-height: 1.5;
  }

  .footer {
    font-size: 9px;
    color: var(--muted2);
    margin-top: 16px;
    text-align: center;
  }

  /* Modal (replaces messagebox) */
  .modal-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.6);
    align-items: center;
    justify-content: center;
    z-index: 100;
  }

  .modal-overlay.show { display: flex; }

  .modal-box {
    background: var(--card);
    border-radius: 8px;
    padding: 28px 32px;
    max-width: 380px;
    text-align: center;
    box-shadow: 0 10px 40px rgba(0,0,0,0.5);
  }

  .modal-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 14px;
  }

  .modal-body {
    font-size: 13px;
    color: var(--text);
    white-space: pre-line;
    line-height: 1.6;
    margin-bottom: 20px;
  }

  .modal-ok {
    background: #0284c7;
    width: 140px;
    padding: 10px 0;
  }
  .modal-ok:hover { background: #0369a1; }

  @media (max-width: 560px) {
    .card { padding: 24px 14px; min-height: auto; }
    .stat-box { width: 100px; height: 70px; }
    .progress-track { width: 100%; }
    input#guessInput { width: 160px; font-size: 20px; }
    button { width: 140px; font-size: 11px; }
    #newGameBtn { width: 100%; }
  }
</style>
</head>
<body>

<div class="main">
  <h1 class="title">🎯 NUMBER GUESSING GAME</h1>
  <p class="subtitle">Guess the secret number before your time runs out!</p>

  <div class="difficulty-row">
    <label for="difficulty">Difficulty:</label>
    <select id="difficulty">
      <option value="Easy">Easy</option>
      <option value="Medium" selected>Medium</option>
      <option value="Hard">Hard</option>
    </select>
  </div>

  <div class="card">
    <div class="range-label" id="rangeLabel">🔢 Guess a number between 1 and 100</div>

    <div class="stats">
      <div class="stat-box">
        <div class="stat-title">ATTEMPTS</div>
        <div class="stat-value" id="attemptValue">0 / 7</div>
      </div>
      <div class="stat-box">
        <div class="stat-title">TIME</div>
        <div class="stat-value" id="timeValue">45s</div>
      </div>
      <div class="stat-box">
        <div class="stat-title">HIGH SCORE</div>
        <div class="stat-value" id="scoreValue">0</div>
      </div>
    </div>

    <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>

    <div class="input-label">ENTER YOUR GUESS</div>
    <input type="number" id="guessInput" autocomplete="off" />

    <div class="buttons">
      <button id="guessBtn">🎯 GUESS</button>
      <button id="hintBtn">💡 HINT</button>
    </div>

    <div class="result-label" id="resultLabel">🚀 Make your first guess!</div>

    <button id="newGameBtn">🔄 NEW GAME</button>
  </div>

  <div class="footer">Press ESC to exit fullscreen</div>
</div>

<div class="modal-overlay" id="modalOverlay">
  <div class="modal-box">
    <div class="modal-title" id="modalTitle"></div>
    <div class="modal-body" id="modalBody"></div>
    <button class="modal-ok" id="modalOk">OK</button>
  </div>
</div>

<script>
(function () {
  "use strict";

  // ================= SETTINGS =================
  const DIFFICULTIES = {
    Easy:   { maxNumber: 50,  attempts: 10, time: 60 },
    Medium: { maxNumber: 100, attempts: 7,  time: 45 },
    Hard:   { maxNumber: 500, attempts: 5,  time: 30 }
  };

  // ================= STATE =================
  let highScore = 0;
  let timerId = null;

  let maxNumber = 100;
  let secretNumber = 0;
  let attempts = 0;
  let maxAttempts = 7;
  let timeLeft = 45;
  let score = 100;
  let hintUsed = false;
  let gameOver = false;

  // ================= DOM REFS =================
  const difficultySelect = document.getElementById("difficulty");
  const rangeLabel = document.getElementById("rangeLabel");
  const attemptValue = document.getElementById("attemptValue");
  const timeValue = document.getElementById("timeValue");
  const scoreValue = document.getElementById("scoreValue");
  const progressFill = document.getElementById("progressFill");
  const guessInput = document.getElementById("guessInput");
  const guessBtn = document.getElementById("guessBtn");
  const hintBtn = document.getElementById("hintBtn");
  const resultLabel = document.getElementById("resultLabel");
  const newGameBtn = document.getElementById("newGameBtn");

  const modalOverlay = document.getElementById("modalOverlay");
  const modalTitle = document.getElementById("modalTitle");
  const modalBody = document.getElementById("modalBody");
  const modalOk = document.getElementById("modalOk");

  // ================= SOUND SYSTEM (Web Audio API replaces winsound) =================
  let audioCtx = null;

  function getAudioCtx() {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === "suspended") {
      audioCtx.resume();
    }
    return audioCtx;
  }

  // frequency in Hz, duration in ms, startAt = ms delay from now
  function beep(frequency, duration, startAt = 0) {
    try {
      const ctx = getAudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = "square";
      osc.frequency.value = frequency;

      const startTime = ctx.currentTime + startAt / 1000;
      const endTime = startTime + duration / 1000;

      gain.gain.setValueAtTime(0.0001, startTime);
      gain.gain.exponentialRampToValueAtTime(0.15, startTime + 0.01);
      gain.gain.exponentialRampToValueAtTime(0.0001, endTime);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start(startTime);
      osc.stop(endTime + 0.02);
    } catch (e) {
      /* ignore audio errors, same as the try/except in the original */
    }
  }

  function soundClick() {
    beep(700, 100);
  }

  function soundWrong() {
    beep(350, 120, 0);
    beep(250, 150, 120);
  }

  function soundHint() {
    beep(700, 100, 0);
    beep(900, 120, 100);
  }

  function soundWin() {
    beep(700, 120, 0);
    beep(900, 120, 120);
    beep(1100, 120, 240);
    beep(1400, 250, 360);
  }

  function soundGameOver() {
    beep(500, 180, 0);
    beep(400, 180, 180);
    beep(300, 300, 360);
  }

  function soundCountdown() {
    beep(1000, 120);
  }

  // ================= MODAL (replaces messagebox.showinfo) =================
  function showModal(title, body) {
    modalTitle.textContent = title;
    modalBody.textContent = body;
    modalOverlay.classList.add("show");
  }

  function hideModal() {
    modalOverlay.classList.remove("show");
  }

  modalOk.addEventListener("click", hideModal);
  modalOverlay.addEventListener("click", (e) => {
    if (e.target === modalOverlay) hideModal();
  });

  // ================= DIFFICULTY CHANGE =================
  difficultySelect.addEventListener("change", () => {
    soundClick();
    if (timerId) {
      clearTimeout(timerId);
      timerId = null;
    }
    newGame();
  });

  // ================= NEW GAME =================
  function newGame() {
    const settings = DIFFICULTIES[difficultySelect.value];

    maxNumber = settings.maxNumber;
    maxAttempts = settings.attempts;
    timeLeft = settings.time;

    secretNumber = Math.floor(Math.random() * maxNumber) + 1;

    attempts = 0;
    score = 100;
    hintUsed = false;
    gameOver = false;

    rangeLabel.textContent = `🔢 Guess a number between 1 and ${maxNumber}`;
    attemptValue.textContent = `0 / ${maxAttempts}`;

    timeValue.textContent = `${timeLeft}s`;
    timeValue.style.color = "var(--green)";

    scoreValue.textContent = String(highScore);

    resultLabel.textContent = "🚀 Make your first guess!";
    resultLabel.style.color = "white";

    guessBtn.disabled = false;
    hintBtn.disabled = false;
    guessInput.disabled = false;

    guessInput.value = "";
    guessInput.focus();

    updateProgress();

    if (timerId) {
      clearTimeout(timerId);
      timerId = null;
    }

    runTimer();
  }

  // ================= TIMER =================
  function runTimer() {
    if (gameOver) return;

    timeValue.textContent = `${timeLeft}s`;

    if (timeLeft <= 10) {
      timeValue.style.color = "var(--red)";
      soundCountdown();
    } else if (timeLeft <= 20) {
      timeValue.style.color = "var(--amber)";
    } else {
      timeValue.style.color = "var(--green)";
    }

    if (timeLeft <= 0) {
      gameOver = true;

      guessBtn.disabled = true;
      hintBtn.disabled = true;
      guessInput.disabled = true;

      resultLabel.textContent = `⏰ TIME'S UP!\nThe number was ${secretNumber}`;
      resultLabel.style.color = "var(--red)";

      soundGameOver();

      showModal("TIME'S UP", `Time's Up!\n\nThe number was ${secretNumber}`);

      return;
    }

    timeLeft -= 1;
    timerId = setTimeout(runTimer, 1000);
  }

  // ================= CHECK GUESS =================
  function checkGuess() {
    if (gameOver) return;

    const value = guessInput.value.trim();

    if (value === "") {
      resultLabel.textContent = "❌ Enter a number!";
      resultLabel.style.color = "#f87171";
      soundWrong();
      return;
    }

    const guess = parseInt(value, 10);

    if (Number.isNaN(guess) || !Number.isInteger(Number(value))) {
      resultLabel.textContent = "❌ Please enter a valid number!";
      resultLabel.style.color = "#f87171";
      soundWrong();
      guessInput.value = "";
      return;
    }

    if (guess < 1 || guess > maxNumber) {
      resultLabel.textContent = `⚠️ Enter number between 1 and ${maxNumber}!`;
      resultLabel.style.color = "#fbbf24";
      soundWrong();
      return;
    }

    soundClick();

    attempts += 1;
    score = Math.max(0, 100 - (attempts - 1) * 10);

    attemptValue.textContent = `${attempts} / ${maxAttempts}`;
    updateProgress();

    // ================= CORRECT =================
    if (guess === secretNumber) {
      gameOver = true;

      let finalScore = score + timeLeft;
      if (hintUsed) finalScore -= 15;
      finalScore = Math.max(0, finalScore);

      if (finalScore > highScore) {
        highScore = finalScore;
      }
      scoreValue.textContent = String(highScore);

      resultLabel.textContent = `🎉 PERFECT!\nYou found ${secretNumber}!\n🏆 Score: ${finalScore}`;
      resultLabel.style.color = "#4ade80";

      guessBtn.disabled = true;
      hintBtn.disabled = true;
      guessInput.disabled = true;

      if (timerId) {
        clearTimeout(timerId);
        timerId = null;
      }

      soundWin();

      showModal(
        "🏆 YOU WON!",
        `Congratulations!\n\nNumber: ${secretNumber}\nAttempts: ${attempts}\nTime left: ${timeLeft}s\nScore: ${finalScore}`
      );

      return;
    }

    // ================= LOW / HIGH =================
    if (guess < secretNumber) {
      resultLabel.textContent = "📉 TOO LOW!\nTry a higher number.";
      resultLabel.style.color = "var(--blue)";
    } else {
      resultLabel.textContent = "📈 TOO HIGH!\nTry a lower number.";
      resultLabel.style.color = "#fb923c";
    }

    soundWrong();

    // ================= GAME OVER (out of attempts) =================
    if (attempts >= maxAttempts) {
      gameOver = true;

      guessBtn.disabled = true;
      hintBtn.disabled = true;
      guessInput.disabled = true;

      if (timerId) {
        clearTimeout(timerId);
        timerId = null;
      }

      resultLabel.textContent = `😔 GAME OVER!\nThe number was ${secretNumber}`;
      resultLabel.style.color = "var(--red)";

      soundGameOver();

      showModal("😔 GAME OVER", `Game Over!\n\nThe correct number was ${secretNumber}`);

      return;
    }

    guessInput.value = "";
    guessInput.focus();
  }

  // ================= HINT =================
  function showHint() {
    if (gameOver) return;
    if (hintUsed) return;

    hintUsed = true;
    soundHint();

    const parity = secretNumber % 2 === 0 ? "EVEN" : "ODD";
    const position = secretNumber <= Math.floor(maxNumber / 2) ? "FIRST HALF" : "SECOND HALF";

    resultLabel.textContent = `💡 HINT\nThe number is ${parity}\nand is in the ${position}.`;
    resultLabel.style.color = "var(--purple2)";

    hintBtn.disabled = true;
  }

  // ================= PROGRESS =================
  function updateProgress() {
    const percentage = attempts / maxAttempts;
    progressFill.style.width = `${Math.min(100, percentage * 100)}%`;
  }

  // ================= EVENTS =================
  guessBtn.addEventListener("click", checkGuess);
  hintBtn.addEventListener("click", showHint);
  newGameBtn.addEventListener("click", newGame);

  guessInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") checkGuess();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && document.activeElement !== guessInput) {
      checkGuess();
    }
    if (e.key === "Escape") {
      if (document.fullscreenElement) {
        document.exitFullscreen().catch(() => {});
      }
    }
  });

  // Optional: enter fullscreen on first user interaction (browsers block auto-fullscreen)
  document.addEventListener(
    "click",
    function enableFullscreenOnce() {
      if (!document.fullscreenElement && document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen().catch(() => {});
      }
      document.removeEventListener("click", enableFullscreenOnce);
    },
    { once: true }
  );

  // ================= INIT =================
  newGame();
})();
</script>

</body>
</html>
