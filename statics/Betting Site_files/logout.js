
function logout()
{
    $.ajax({
        url: 'logout',
        type: "get",
      });
}