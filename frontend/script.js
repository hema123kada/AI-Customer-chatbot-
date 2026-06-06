async function sendMessage() {

    let input = document.getElementById("user-input");

    let message = input.value;

    if (!message) return;

    let chatBox = document.getElementById("chat-box");

    // Show user message
    chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;

    try {

        const response = await fetch("http://127.0.0.1:5000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        // Show bot response
        chatBox.innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;

    } catch (error) {

        console.log(error);

        chatBox.innerHTML += `<p style="color:red;"><b>Error:</b> Backend connection failed</p>`;
    }

    input.value = "";
}