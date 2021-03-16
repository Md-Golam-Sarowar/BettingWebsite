function authenticateuser() {
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;

    Data = {"username" : username, "password" : password}

    $.ajax({
        url: 'http://127.0.0.1:8000/login',
        type: "post",
        data: Data,
        dataType: 'json',
        success: function (data) {
            if(data["status"] == 200)
            {
                window.location = data["base_dir"]+"/home";
            }
            else if (data["status"] == 500)
            {
                alert("please provide valid username and password");
            }
        }
      });
  }