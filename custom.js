
function POST(){
    var username = document.getElementById('username').value;
    var pass = document.getElementById('pass').value;

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", pass);

    fetch('/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: formData
        })
        .then(response => response.text())
        .then(data => console.log('Успешно обработано:', data))
        .catch(error => console.error('Ошибка обработки:', error));
}
