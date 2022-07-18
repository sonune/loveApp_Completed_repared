function Realtime() {
    let newDate = new Date()
    let minutes = newDate.getMinutes()
    let hours = newDate.getHours()
    let second = newDate.getSeconds()
    let today = new Date();
    // let date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
    let date = today.getDate() + '-' + (today.getMonth() + 1) + '-' +  today.getFullYear();
    let time = hours + ":" + minutes + ":" + second ;
    return(date + ',' + time)
}
setInterval(Realtime, 1000);



let validate = false;
// let ws = new WebSocket('ws://127.0.0.1:8000/ws/loveChat/')
let ws = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/loveChat/'
    )
ws.addEventListener('open', () => {
    console.log('Open connection')
    validate = true;
    ws.send(JSON.stringify({
        'command': 'join',
        'groupname': 'loveBirds'
    }))
})
let button = document.getElementById('input-btn')
button.addEventListener('click', () => {
    if (validate) {
        const message = document.getElementById('input-message').value;
        ws.send(JSON.stringify({
            'command': 'send',
            'message': message
        }))
        console.log(message)
        document.getElementById('input-message').value = '';
    } else {
        console.log('NOT')
    }
})
ws.onmessage = (e) => {
    const data1 = JSON.parse(e.data)
        if (data1.message) {
        const message = data1.message
        const user = data1.user
        console.log(message)
        console.log(user)
        let a = `
        <div class="a-chat">
                <div class="username-message" style="font-family: 'Merienda', cursive;font-size: 0.8em;">${Realtime()}</div>
                <div class="username-message">${user}</div>
                <div class="chat-message">${message}</div>
            </div> <br>
        `

        let chat = document.getElementsByClassName('chat-content')[0];
        chat.innerHTML += a
    }
}

ws.onclose = (e) => {
    location.reload()
}

ws.onerror = (e) => {
    location.reload()
}



