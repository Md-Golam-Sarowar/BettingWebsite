
function send(elem)
{
    row = elem.parentNode.parentNode.parentNode;
    var id, username, password, role;

    username = row.querySelector("#username").value;
    password = row.querySelector("#password").value;
    limit = row.querySelector("#limit").value;
    role = row.querySelector("#role").value;

    for (let i in row.cells)
    {
        if(i==0)
        {
            id = row.cells[i].textContent;
        }

    }
    
    var intId = parseInt(id, 10);

    Data = { "username" : username, "password" : password, "role" : role, "limit": limit}

    $.ajax({
        url: 'updateCredential/'+intId,
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


function del(elem)
{
    row = elem.parentNode.parentNode.parentNode;
    adminId = row.querySelector("#adminId").textContent;

    table = row.parentNode;
    var rowNo;

    $.ajax({
        url: 'deleteCredential/'+adminId,
        type: "get",
      });

    for(let i in table.rows)
    {
        id = table.rows[i].querySelector("#adminId").textContent;
        if(adminId == id)
        {
            rowNo = i;
            break;
        }
    }

    table.deleteRow(rowNo);

    alert("Deleted Successfully!");

}


function generate()
{
    generateUser = document.getElementById("generateUser").value;

    $.ajax({
        url: 'generatecredentials/'+generateUser,
        type: "get",
        success: function (data) {
            if(data["status"] == 200)
            {
                alert("Successfully generated");
                window.location = data["base_dir"]+"/dashboard";
            }
        }
      });
}