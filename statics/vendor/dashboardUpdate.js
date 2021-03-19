
function send(elem)
{
    row = elem.parentNode.parentNode.parentNode;
    var id, username, password, role;

    username = row.querySelector("#username").value;
    password = row.querySelector("#password").value;
    role = row.querySelector("#role").value;

    for (let i in row.cells)
    {
        if(i==0)
        {
            id = row.cells[i].textContent;
        }

    }
    
    var intId = parseInt(id, 10);

    Data = { "username" : username, "password" : password, "role" : role}

    $.ajax({
        url: 'http://127.0.0.1:8000/updateCredential/'+intId,
        type: "post",
        data: Data,
        dataType: 'json',
        success: function (data) {
            if(data["status"] == 200)
            {
                alert("Successfully updated");
                window.location = data["base_dir"]+"/dashboard";
            }
        }
      });
}