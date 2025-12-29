function runSearch() {
    const query = document.getElementById('query').value;
    const results = document.getElementById('results');

    if(query.trim() === "") {
        results.innerHTML = "<p>Please enter a topic to search.</p>";
        return;
    }

    // Simulated search result
    results.innerHTML = `<p>Searching for: <strong>${query}</strong> ...</p>`;

    setTimeout(() => {
        results.innerHTML = `<p>Results for <strong>${query}</strong> will appear here. (Simulated)</p>`;
    }, 1500);
}
function runSearch() {
    const query = document.getElementById('query').value;
    const results = document.getElementById('results');

    if(query.trim() === "") {
        results.innerHTML = "<p>Please enter a topic to search.</p>";
        return;
    }

    results.innerHTML = `<p>Searching for: <strong>${query}</strong> ...</p>`;

    fetch(`/search/?query=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            results.innerHTML = `<p>${data.result}</p>`;
        })
        .catch(error => {
            results.innerHTML = "<p>Error fetching results.</p>";
            console.error(error);
        });
}
