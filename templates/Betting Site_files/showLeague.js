function showLeague(){
    Data = {"url":"https://mybookie.ag/sportsbook/mlb/spring-training/"}

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