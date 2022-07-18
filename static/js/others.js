function toggle3(){
    var a = document.getElementById("main-recent-chats");
    var b = document.getElementById('fake-recent-chats')
    if (a.style.display === "none" & b.style.display == "block") {
        a.style.display = "block";
        b.style.display = 'none';
    } else {
        a.style.display = "none";
        b.style.display = 'block';
    }
}




function hatt() {
    window.location.href = "https://www.jackandjill.in/";
}
function toggle2(){
    var a = document.getElementById("main-chat");
    var b = document.getElementById('footer')
    if (a.style.display === "none" & b.style.display == "flex") {
        a.style.display = "flex";
        b.style.display = 'none';
    } else {
        a.style.display = "none";
        b.style.display = 'flex';
    }
}

function Main() {
    window.location.href = "https://jackjill.pythonanywhere.com/Home";
}
function log() {
    window.location.href = "https://jackjill.pythonanywhere.com/logdetect";
}


function Meet() {
window.location.href = 'https://jackjill.pythonanywhere.com/Meet'
    
}