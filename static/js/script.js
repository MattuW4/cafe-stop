document.addEventListener('DOMContentLoaded', closeAlerts);

function closeAlerts () {
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);
};

define('summernote/settings', function () {

    var settings = {
   
      version: '0.8.20.0',
    }

    options: {

        width: 50%;                // set editor width
  
        height: 10rem;                 // set editor height, ex) 300
}