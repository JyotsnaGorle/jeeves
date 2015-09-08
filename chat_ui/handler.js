function addChat(message) {
    message = JSON.parse(message);
    var person = message.person;
    console.log(person);
    var msg = message.msg;
    var alignment_out = "left";
    var alignment_in = "right";

    var icon = 'b';
    var jeeves_icon = 'a';

    var chat_screen = document.getElementById("chat_screen");
    var div = document.createElement('div');

    if (person === 'jeeves') {
        alignment_out = 'right';
        alignment_in = 'left';
        icon = jeeves_icon;
    }
    div.innerHTML = "<div class='chat clear'><div class='clear' ><div class='icon-container " + alignment_out + "'><img src='images/" + icon + ".png'></div><div class='" + person + " " + alignment_in + "'><p>" + msg + "</p></div></div></div>";
    chat_screen.appendChild(div);
}
