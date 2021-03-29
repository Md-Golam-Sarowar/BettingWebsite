function showLeague(url){
    Data = {"url":url}

    $.ajax({
        url: 'leagueInformation',
        type: "post",
        data: Data,
        dataType: 'json',
      });
}