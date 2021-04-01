
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
    window.location = "sports";
}


function teaser()
{

    $.ajax({
        url: 'teaser',
        type: "get",
      });
}



function collectcheckedlist()
{
    sportsDiv = document.getElementById("sportsDiv");
    checkboxes = sportsDiv.getElementsByClassName("checkbox checkbox-primary");
    var listOfLinks = [];
    for(var i=0; i<checkboxes.length;i++)
    {
        exactcheckbox = checkboxes[i].getElementsByClassName("c_league");
        if(exactcheckbox[0].checked == true)
        {
            listOfLinks.push(checkboxes[i].getElementsByTagName("Label")[0].getElementsByTagName("a")[0].attributes.value.value);
        }
    }

    if(listOfLinks.length>0)
    {
        window.location = "checkedLeagues/"+listOfLinks;
    }
    else
    {
        alert("No Leagues Selected!");
    }

}
