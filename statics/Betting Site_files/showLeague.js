
function showLeagueInfo(leagueName)
{
    dataurl = "";
    if(leagueName == "MLB - Spring Training Odds")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/spring-training/"
    }
    else if(leagueName == "MLB - Content Props")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/contest-props/"
    }

    Data = {"url": dataUrl};

    $.ajax({
        url: '../scappingLeagueInfo',
        type: "post",
        data: Data,
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