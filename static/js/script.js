document.addEventListener("DOMContentLoaded", () => {
    // Timer for dismissal of popup messages
    setTimeout(function () {
      $("#msg").alert("close");
    }, 2500);
  });