
async function POST(){
    var username = document.getElementById('username').value;
    var pass = document.getElementById('pass').value;

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", pass);
    if(pass.length < 6){
        document.getElementById("666").style.display = 'inline';
    }

    const Z = await fetch('/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: formData
        });
        //.then(response => response.status)
        //.then(data => console.log('Успешно обработано:',data))
        //.catch(error => console.error('Ошибка обработки:', error));

    const json = await Z.json();
    if (json["status_code"] == 418){
        document.getElementById("555").style.display = 'inline';
        document.getElementById("666").style.display = 'none';
    }
    if (json["status_code"] == 200){
        window.location.href = "/личный-кабинет.html";
    }

}
