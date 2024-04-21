function calculatePoints() {
    let startTime, endTime;

    startTime = new Date(document.getElementById('start-time').value);
    if (startTime == "Invalid Date") {
        startTime = new Date();
    }

    endTime = new Date(document.getElementById('end-time').value);
    if (endTime == "Invalid Date") {
        endTime = new Date();
    }

    let initialPoints = parseInt(document.getElementById('initial-points').value);
    if (isNaN(initialPoints)) {
        initialPoints = 0;
    }

    let maxPoints = parseInt(document.getElementById('max-points').value);
    if (isNaN(maxPoints)) {
        maxPoints = 0;
    }

    let elapsedMinutes = (endTime - startTime) / (1000 * 60);
    let pointsPerFiveMinutes = Math.floor(elapsedMinutes / 5);
    let totalPoints = initialPoints + pointsPerFiveMinutes;

    document.getElementById('result').innerText = `LP Total: ${totalPoints}`;

    let targetPoints = maxPoints - pointsPerFiveMinutes;
    document.getElementById('target').innerText = `LP Target: ${targetPoints}`;

    // point countdown calculation
    let pointsNeeded = maxPoints - initialPoints;
    console.log(maxPoints);
    console.log(initialPoints);
    let minutesToFull = pointsNeeded * 5;
    console.log(minutesToFull);
    let fullTime = new Date(startTime.getTime() + minutesToFull * 60 * 1000);
    console.log(startTime);
    console.log(fullTime);
    console.log((fullTime - startTime) / (60 * 1000));

    document.getElementById('countdown-date').innerText = `LP will be full at: ${fullTime.toLocaleString()}`;
    document.getElementById('countdown-date').style.display = 'block';

    // points to leave
    document.getElementById('gained').innerText = `LP Gained: ${pointsPerFiveMinutes}`;

    // Update the count down every 1 second
    var x = setInterval(function() {
        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var distance = fullTime - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="demo"
        document.getElementById("countdown-clock").innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
        document.getElementById('countdown-clock').style.display = 'block';

        // If the count down is finished, write some text
        if (distance < 0) {
            clearInterval(x);
            document.getElementById("countdown-clock").innerHTML = "LP is full.";
        }
    }, 1000);
}
