var h1 = document.getElementById('chronotime'),
    start = document.getElementById('start'),
    stop = document.getElementById('stop'),
    clear = document.getElementById('clear'),
    continue_button = document.getElementById('continue'),
    seconds = 0, minutes = 0, hours = 0,
    t,
    now;

function add() {
    seconds++;
    if (seconds >= 60) {
        seconds = 0;
        minutes++;
        if (minutes >= 60) {
            minutes = 0;
            hours++;
        }
    }

    h1.textContent = (hours ? (hours > 9 ? hours : "0" + hours) : "00") + ":" + (minutes ? (minutes > 9 ? minutes : "0" + minutes) : "00") + ":" + (seconds > 9 ? seconds : "0" + seconds);

    timer();
}

function timer() {
    t = setTimeout(add, 1000);
}

/* Start button */
start.onclick = function () {
	start.setAttribute("display",'none')
	continue_button.setAttribute('display','none')
	stop.setAttribute('display','block')
    now = new Date();
    timer();
};

/* Continue button*/
continue_button.onclick = function (){
	start.setAttribute("display",'none')
	continue_button.setAttribute('display','none')
	stop.setAttribute('display','block')
	timer();
};

/* Stop button */
stop.onclick = function () {
	start.setAttribute("display",'none')
	continue_button.setAttribute('display','block')
	stop.setAttribute('display','none')
    clearTimeout(t);
}

/* Clear button */
clear.onclick = function () {
    h1.textContent = "00:00:00";
    seconds = 0;
    minutes = 0;
    hours = 0;
}

function initClock() {
    document.getElementById("buttonclock").setAttribute("display", "none")
    document.getElementById("clock-section").setAttribute('display', 'block')
}