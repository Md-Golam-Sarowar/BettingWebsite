function authenticateuser() {
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;

    Data = {"username" : username, "password" : password}

    $.ajax({
        url: 'login',
        type: "post",
        data: Data,
        dataType: 'json',
        success: function (data) {
            if(data["status"] == 200)
            {
                window.location = "/home";
            }
            else if (data["status"] == 500)
            {
                document.getElementById("username").value = "";
                document.getElementById("password").value = "";
                alert("please provide valid username and password");
            }
        }
      });
  }