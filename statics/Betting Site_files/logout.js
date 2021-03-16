
function logout()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/logout',
        type: "get",
      });
}