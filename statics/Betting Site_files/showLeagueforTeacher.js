window.onload = function ()
{
  var allIds = [];
  ids = document.getElementById("totalids").innerText;
  splitedids = ids.split(",")

  for(var i=1; i<splitedids.length;i++)
  {
    splited = splitedids[i].split("'");
    allIds.push(splited[1]);
  }

  payload = {url: allIds};

  $.ajax({
      url: '../scappingLeagueInfoforTeacher',
      type: "post",
      data: payload,
      dataType: 'json',
      success: function (returneddata) {
        if(returneddata["status"] == 200)
        {
            document.getElementById("main-container").innerHTML += returneddata["data"];
        }
        else if (returneddata["status"] == 500)
        {
            alert("No lines available");
        }
    }
    });

}