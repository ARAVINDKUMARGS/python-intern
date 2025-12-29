function searchTopic() {
    const topic = document.getElementById("topic").value;
    fetch(`/search/?topic=${topic}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = data.result;
        });
}
