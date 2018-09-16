function sendAlert() {
    const xhr = new XMLHttpRequest();
    var t = document.getElementById("url_text_field").value;
    alert(t);
    console.log(t);
    xhr.open('POST', 'http://localhost:5000/upload/');
    xhr.send(t);
}

// function get_boolean(results):
//     if (results) {
//         return false
//     }
//     return true
