
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