let minutes = document.getElementById(`p-tegi`).textContent;
function countDownTimer() {
    const currentTime = Date.now();
    const remainingTime = futureTime - currentTime;
}
let totalSeconds = minutes * 60;

function updateCountdown() {
    if (totalSeconds <= 0) {
        // Countdown has ended, redirect to another page
        window.location.href = 'https://google.com';
        return;
    }
    
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    
    // Format minutes and seconds with leading zeros
    const formattedMinutes = String(minutes).padStart(2, '0');
    const formattedSeconds = String(seconds).padStart(2, '0');
    
    document.querySelector('.minutes-number').innerText = formattedMinutes;
    document.querySelector('.seconds-number').innerText = formattedSeconds;
    
    totalSeconds--;
}

// Update countdown every second
setInterval(updateCountdown, 1000);

// Initial update
updateCountdown();