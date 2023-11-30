function sendRequest() {
    var apiCall = document.getElementById('apiCall').value;
    var productName = document.getElementById('productName').value;
    fetch('http://localhost:80' + apiCall + productName)
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            document.getElementById('response').textContent = 'Error: ' + error;
        });
}