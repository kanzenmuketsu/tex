
async function registration(){
    var username = document.getElementById('reg_username').value;
    var email = document.getElementById('email').value;
    var pass1 = document.getElementById('reg_pass1').value;
    var pass2 = document.getElementById('reg_pass2').value;
    var email_id = await getCookie('id')
    var email_code = document.getElementById('email_code').value;

    if (email_code == "") {
         email_code = '0'
    }





    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("email", email);
    formData.append("password1", pass1);
    formData.append("password2", pass2);
    formData.append("email_id", email_id);
    formData.append("email_code", email_code);

    const ZZ = await fetch('/register', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: formData
        });
        //.then(response => response.status)
        //.then(data => console.log('Успешно обработано:',data))
        //.catch(error => console.error('Ошибка обработки:', error));

    const json = await ZZ.json();

    if (json["status_code"] == 409){
        document.getElementById("dont_match").style.display = 'inline';
    }
    if (json["status_code"] == 103){
        document.getElementById("dont_match").style.display = 'none';
        document.getElementById("start-form").style.display = 'none';
        document.getElementById("code").style.display = 'inline';
    }
    if (json["status_code"] == 423){
        document.getElementById("dont_match").style.display = 'none';
        document.getElementById("invalid_code").style.display = 'inline';
    }
    if (json["status_code"] == 400){
        document.getElementById("already_exist").style.display = 'inline';
    }
    if (json["status_code"] == 200){
        window.location.href = "/личный-кабинет.html";
    }

}
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
async function getCookie(name) {
  let cookie = {};
  document.cookie.split(';').forEach(function(el) {
    let split = el.split('=');
    cookie[split[0].trim()] = split.slice(1).join("=");
  })
  return cookie[name];
}

async function LOGOUT(){
    const ZZZ = await fetch('/logout', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: 'logout'
        });
    const json = await ZZZ.json();
    if (json["status_code"] == 200){
        window.location.href = "/index.html";
    }
    else{
        alert('error')
       }
}
async function showpopup(){
    if(document.getElementById('btm').innerText == 'Нет в наличии'){
        return false;
    }
    document.getElementById("popup-overlay").style.display = 'block';
    document.getElementById("prev").style.display = 'none';
    document.getElementById("next").style.display = 'none';
    }

async function buy(){

    var product_name = document.getElementById('product_name').innerText;
    var amount = document.getElementById('amount').value;

    const formData = new URLSearchParams();
    formData.append("product_name", product_name);
    formData.append("amount", amount);

    const Z = await fetch('/add_to_cart', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: formData
        });

    const json = await Z.json();
    if (json["status_code"] == 418){
    }
    if (json["status_code"] == 200){
        hidePopup();
        alert('ok');
    }
}

async function hidePopup() {
  document.getElementById("popup-overlay").style.display = 'none';
  document.getElementById("prev").style.display = 'inline';
  document.getElementById("next").style.display = 'inline';
}
