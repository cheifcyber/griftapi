function sendRequest() {
    var apiCall = document.getElementById('apiCall').value;
    var productName = document.getElementById('productName').value;
    fetch('https://grift.vuln.dad' + apiCall + productName)
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            document.getElementById('response').textContent = 'Error: ' + error;
        });
}