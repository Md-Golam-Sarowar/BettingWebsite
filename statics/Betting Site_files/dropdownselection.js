
function straight()
{
    $.ajax({
        url: 'sports',
        type: "get",
      });
}


function parlay()
{
    console.log("this");
    window.location = "/parlay";
}


function teaser()
{

    $.ajax({
        url: 'teaser',
        type: "get",
      });
}


window.onload = function()
{
    leaguename = '{{name}}';

    console.log(leaguename);

    alert(leaguename);
}