var start_button = document.getElementById('buttonclock'),
    clock_section = [document.getElementById('base-button'),document.getElementById('chronotime2')],
    h1 = document.getElementById('chronotime'),
    start = document.getElementById('start'),
    stop = document.getElementById('stop'),
    clear = document.getElementById('clear'),
    continue_button = document.getElementById('continue'),
    seconds = 0, minutes = 0, hours = 0,
    t,
    now;

/*
window.onload=function () {
    start_button=document.getElementById('buttonclock'),
    h1 = document.getElementById('chronotime'),
    start = document.getElementById('start'),
    stop = document.getElementById('stop'),
    clear = document.getElementById('clear'),
    continue_button = document.getElementById('continue'),
    e.innerHTML='Found you';
};
*/

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
    start.setAttribute("style", 'display: none');
    continue_button.setAttribute('style', 'display: none');
    stop.setAttribute('style', 'display: block');
    now = new Date();
    timer();
};

/* Continue button*/
continue_button.onclick = function () {
    start.setAttribute("style", 'display: none');
    continue_button.setAttribute('style', 'display: none');
    stop.setAttribute('style', 'display: block');
    timer();
};

/* Stop button */
stop.onclick = function () {
    start.setAttribute("style", 'display: none');
    continue_button.setAttribute('style', 'display: block');
    stop.setAttribute('style', 'display: none');
    clearTimeout(t);
}

/* Clear button */
clear.onclick = function () {
    h1.textContent = "00:00:00";
    seconds = 0;
    minutes = 0;
    hours = 0;
};

start_button.onclick = function () {
    document.getElementById("buttonclock").setAttribute("style", "display: none");
    /*var element = document.getElementById("buttonclock");
    element.parentNode.removeChild(element);*/
    document.getElementById("base-button").setAttribute("style", "display: block");
    document.getElementById("chronotime2").setAttribute('style', 'display: block');
};