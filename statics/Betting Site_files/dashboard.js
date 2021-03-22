
function dashboard()
{
    $.ajax({
        url: 'adminAccess',
        type: "get",
        datatype: JSON,
        success: function (data) {
            if(data["data"]["role"] == "admin")
            {
                window.location = "/dashboard";
            }
            else if(data["data"]["role"] == "user")
            {
                alert("You are not an admin!");
            }
        }
      });
}