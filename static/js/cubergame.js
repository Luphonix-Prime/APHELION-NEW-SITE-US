const gameArena = document.querySelector('.game-arena');
const shield = document.querySelector('.security-shield');
const scoreValue = document.querySelector('.score-value');
const healthValue = document.querySelector('.health-value');
const gameOver = document.querySelector('.game-over');
const restartButton = document.querySelector('.restart-button');

let score = 0;
let health = 100;
let gameActive = true;

function createVirus() {
    if (!gameActive) return;
    
    const virus = document.createElement('div');
    virus.classList.add('virus');
    virus.style.left = Math.random() * (gameArena.offsetWidth - 20) + 'px';
    virus.style.top = '-20px';
    gameArena.appendChild(virus);
    
    const speed = 2 + Math.random() * 2;
    
    function moveVirus() {
        if (!gameActive) return;
        
        const top = parseFloat(virus.style.top);
        if (top > gameArena.offsetHeight) {
            virus.remove();
            updateHealth(-10);
        } else {
            virus.style.top = (top + speed) + 'px';
            requestAnimationFrame(moveVirus);
        }
    }
    
    moveVirus();
    virus.addEventListener('click', () => {
        virus.remove();
        updateScore(10);
        createDefenseEffect(virus.offsetLeft, virus.offsetTop);
    });
}

function updateScore(points) {
    score += points;
    scoreValue.textContent = score;
}

function updateHealth(change) {
    health = Math.max(0, health + change);
    healthValue.textContent = health + '%';
    
    if (health <= 0) {
        endGame();
    }
}

function createDefenseEffect(x, y) {
    const effect = document.createElement('div');
    effect.classList.add('defense-effect');
    effect.style.left = x + 'px';
    effect.style.top = y + 'px';
    gameArena.appendChild(effect);
    
    setTimeout(() => effect.remove(), 1000);
}

function endGame() {
    gameActive = false;
    gameOver.classList.remove('hidden');
    gameOver.classList.add('flex');
    document.querySelector('.final-score').textContent = score;
}

function startGame() {
    score = 0;
    health = 100;
    gameActive = true;
    scoreValue.textContent = '0';
    healthValue.textContent = '100%';
    gameOver.classList.add('hidden');
    gameOver.classList.remove('flex');
    
    // Clear existing viruses
    document.querySelectorAll('.virus').forEach(v => v.remove());
    
    // Start virus generation
    setInterval(createVirus, 2000);
}

restartButton.addEventListener('click', startGame);
startGame();