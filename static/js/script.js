document.addEventListener('DOMContentLoaded', closeAlerts);

// Timer for dismissal of popup messages
function closeAlerts () {
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);
}