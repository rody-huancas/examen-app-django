const messageContainer = document.getElementById("message-container");

if (messageContainer) {
    messageContainer.style.display = "block";

    setTimeout(function () {
        messageContainer.style.display = "none";
    }, 3000);
}
