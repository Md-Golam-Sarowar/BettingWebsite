
function showLeagueInfo(leagueName)
{
    dataUrl = "";
    if(leagueName == "MLB - Spring Training Odds")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/spring-training/"
    }
    else if(leagueName == "MLB - Content Props")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/contest-props/"
    }
    else if(leagueName == "MLB - 2021 World Series Odds")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/world-series/"
    }
    else if(leagueName == "MLB - AL Pennant")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/american-league/"
    }
    else if(leagueName == "MLB - NL Pennant")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/national-league/"
    }
    else if(leagueName == "MLB - AL Divisional")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/american-league-divisions/"
    }
    else if(leagueName == "MLB - NL Divisional")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/national-league-divisions/"
    }
    else if(leagueName == "MLB - Regular Season Wins")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/regular-season-wins/"
    }
    else if(leagueName == "MLB - Regular Season Award")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mlb/season-awards/"
    }
    else if(leagueName == "Football National Championship Odds")
    {
      dataUrl = "https://mybookie.ag/sportsbook/college-football/championship/"
    }
    else if(leagueName == "Heisman Trophy Winner")
    {
      dataUrl = "https://mybookie.ag/sportsbook/college-football/heisman-trophy/"
    }
    else if(leagueName == "Super Bowl 56 Odds to win")
    {
      dataUrl = "https://mybookie.ag/sportsbook/nfl/super-bowl/"
    }
    else if(leagueName == "NFC Championship Odds")
    {
      dataUrl = "https://mybookie.ag/sportsbook/nfl/nfc/"
    }
    else if(leagueName == "AFC Championship Odds")
    {
      dataUrl = "https://mybookie.ag/sportsbook/nfl/afc/"
    }
    else if(leagueName == "AFC Divisional Odds")
    {
      dataUrl = "https://mybookie.ag/sportsbook/nfl/afc/#accordionBets221"
    }
    else if(leagueName == "AFC Divisional Odds")
    {
      dataUrl = "https://mybookie.ag/sportsbook/nfl/nfc/#accordionBets790"
    }
    else if(leagueName == "NFC Draft Props 2021")
    {
      dataUrl = "https://mybookie.ag/sportsbook/nfl/draft/"
    }
    else if(leagueName == "Indian Premier League")
    {
      dataUrl = "https://mybookie.ag/sportsbook/indian-premier-league/"
    }
    else if(leagueName == "Futures")
    {
      dataUrl = "https://mybookie.ag/sportsbook/cricket/#accordionBets1331"
    }
    else if(leagueName == "Elite Eight Odds March Madness")
    {
      dataUrl = "https://mybookie.ag/sportsbook/ncaa-basketball/march-madness/#accordionBets4"
    }
    else if(leagueName == "NCAA 1st Half Lines")
    {
      dataUrl = "https://mybookie.ag/sportsbook/ncaa-basketball/1st-half/"
    }
    else if(leagueName == "Women's March Madness Lines")
    {
      dataUrl = "https://mybookie.ag/sportsbook/ncaa-basketball-women/"
    }
    else if(leagueName == "France - Ligue A, Women")
    {
      dataUrl = "https://mybookie.ag/sportsbook/france-ligue-a-volleyball/#accordionBets4871"
    }
    else if(leagueName == "Korea Republic - V League")
    {
      dataUrl = "https://mybookie.ag/sportsbook/korea-v-league-volleyball/"
    }
    else if(leagueName == "Russia - Pro League")
    {
      dataUrl = "https://mybookie.ag/sportsbook/russia-pro-league/"
    }
    else if(leagueName == "Russia - Super League")
    {
      dataUrl = "https://mybookie.ag/sportsbook/russia-super-league-volleyball/"
    }
    else if(leagueName == "UFC Lines")
    {
      dataUrl = "https://mybookie.ag/sportsbook/ufc/"
    }
    else if(leagueName == "UFC Upcoming Events")
    {
      dataUrl = "https://mybookie.ag/sportsbook/ufc/#accordionBets3778"
    }
    else if(leagueName == "Bellator Odds")
    {
      dataUrl = "https://mybookie.ag/sportsbook/bellator/"
    }
    else if(leagueName == "Conor McGregor Odds")
    {
      dataUrl = "https://mybookie.ag/sportsbook/conor-mcgregor/"
    }
    else if(leagueName == "MMA Specials")
    {
      dataUrl = "https://mybookie.ag/sportsbook/mma/specials/"
    }
    else if(leagueName == "China - CBA")
    {
      dataUrl = "https://mybookie.ag/sportsbook/china-cba/"
    }
    else if(leagueName == "England - BBL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/croatia-premier-league/"
    }
    else if(leagueName == "France - Pro A")
    {
      dataUrl = "https://mybookie.ag/sportsbook/france-lnb/"
    }
    else if(leagueName == "Germany - BBL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/germany-bbl/"
    }
    else if(leagueName == "Greece - A1")
    {
      dataUrl = "https://mybookie.ag/sportsbook/greece-a1/"
    }
    else if(leagueName == "International Events ABA League")
    {
      dataUrl = "https://mybookie.ag/sportsbook/aba-league/"
    }
    else if(leagueName == "Lithuania - LKL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/lithuania-lkl/"
    }
    else if(leagueName == "Slovenia - Premier A League")
    {
      dataUrl = "https://mybookie.ag/sportsbook/slovenia-premier-a-basketball/"
    }
    else if(leagueName == "South Korea - KBL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/south-korea-kbl/"
    }
    else if(leagueName == "Sweden - Basketligan")
    {
      dataUrl = "https://mybookie.ag/sportsbook/sweden-basketball-league/"
    }
    else if(leagueName == "USA - NBA Player Props")
    {
      dataUrl = "https://mybookie.ag/sportsbook/nba/player-props/#accordionBets123"
    }
    else if(leagueName == "Uruguay - Uruguay (LUB)")
    {
      dataUrl = "https://mybookie.ag/sportsbook/nba/"
    }
    else if(leagueName == "ATP Lines")
    {
      dataUrl = "https://mybookie.ag/sportsbook/atp/"
    }
    else if(leagueName == "ATP Doubles")
    {
      dataUrl = "https://mybookie.ag/sportsbook/atp/#accordionBets3546"
    }
    else if(leagueName == "WTA Lines")
    {
      dataUrl = "https://mybookie.ag/sportsbook/wta/"
    }
    else if(leagueName == "WTA Doubles")
    {
      dataUrl = "https://mybookie.ag/sportsbook/wta/#accordionBets3547"
    }
    else if(leagueName == "ATP Challenger")
    {
      dataUrl = "https://mybookie.ag/sportsbook/atp-challenger/"
    }
    else if(leagueName == "ATP Challenger Doubles")
    {
      dataUrl = "https://mybookie.ag/sportsbook/atp-challenger/#accordionBets3578"
    }
    else if(leagueName == "ITF Men")
    {
      dataUrl = "https://mybookie.ag/sportsbook/itf/"
    }
    else if(leagueName == "ITF Men Doubles")
    {
      dataUrl = "https://mybookie.ag/sportsbook/itf/#accordionBets4908"
    }
    else if(leagueName == "ITF Women")
    {
      dataUrl = "https://mybookie.ag/sportsbook/itf/#accordionBets3551"
    }
    else if(leagueName == "ITF Womens Doubles")
    {
      dataUrl = "https://mybookie.ag/sportsbook/itf/#accordionBets4909"
    }
    else if(leagueName == "Australian Open Odds 2022")
    {
      dataUrl = "https://mybookie.ag/sportsbook/australian-open/"
    }
    else if(leagueName == "Wimbledon Odds 2021")
    {
      dataUrl = "https://mybookie.ag/sportsbook/wimbledon/"
    }
    else if(leagueName == "U.S.Open Odds 2021")
    {
      dataUrl = "https://mybookie.ag/sportsbook/us-open/#accordionBets3309"
    }
    else if(leagueName == "French Open Odds to win 2021")
    {
      dataUrl = "https://mybookie.ag/sportsbook/french-open/#accordionBets3307"
    }
    else if(leagueName == "Austria - EHL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/austria-ehl/"
    }
    else if(leagueName == "Belarus - Extra League")
    {
      dataUrl = "https://mybookie.ag/sportsbook/belarus-extra-league/"
    }
    else if(leagueName == "Canada - WHL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/canada-whl/"
    }
    else if(leagueName == "Canada - Quebec Major JR HL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/quebec-major-league/"
    }
    else if(leagueName == "Czech Republic - First League")
    {
      dataUrl = "https://mybookie.ag/sportsbook/czech-republic-first-league-hockey/"
    }
    else if(leagueName == "Finland - LIIGA")
    {
      dataUrl = "https://mybookie.ag/sportsbook/finland-liiga/"
    }
    else if(leagueName == "Germany - DEL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/germany-del/"
    }
    else if(leagueName == "Sweden - SHL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/sweden-shl/"
    }
    else if(leagueName == "Russia - MHL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/russia-mhl/"
    }
    else if(leagueName == "Russia - VHL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/russia-vhl/"
    }
    else if(leagueName == "Russia - KHL")
    {
      dataUrl = "https://mybookie.ag/sportsbook/russia-khl/"
    }
    else if(leagueName == "Switzerland - Swiss League")
    {
      dataUrl = "https://mybookie.ag/sportsbook/switzerland-swiss-league/"
    }
    else if(leagueName == "Switzerland - National League")
    {
      dataUrl = "https://mybookie.ag/sportsbook/switzerland-national-league/"
    }
    else if(leagueName == "U20 World Championship")
    {
      dataUrl = "https://mybookie.ag/sportsbook/world-championship-hockey/"
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


window.onload = function ()
{
  var allIds = [];
  ids = document.getElementById("totalids").innerText;
  splitedids = ids.split(",")

  for(var i=0; i<splitedids.length;i++)
  {
    splited = splitedids[i].split("'");
    allIds.push(splited[1]);
  }

  payload = {url: allIds};

  $.ajax({
      url: '../scappingLeagueInfoforContinue',
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