function displayTime() {
    const d = new Date();
    document.getElementById("htime").firstChild.nodeValue = "Hora: " + d.toLocaleTimeString();
    document.getElementById('mda').innerHTML = "&copy; " + d.getFullYear();
}
setInterval(displayTime, 1)