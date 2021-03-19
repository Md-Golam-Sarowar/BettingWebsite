
function dashboard()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/adminAccess',
        type: "get",
        datatype: JSON,
        success: function (data) {
            if(data["data"]["role"] == "admin")
            {
                window.location = data["base_dir"]+"/dashboard";
            }
            else if(data["data"]["role"] == "user")
            {
                alert("You are not an admin!");
            }
        }
      });
}