// assuming url is http://127.0.0.1:8080/web/

// Send POST Request to Server and retrieve JSON file of video links
function SearchProcess() {
    var searchitem = $('#myform').serialize();
    $.post("http://localhost:3001/action", searchitem, function( data ) {
        //data is JSON file of video links
        console.log(data);
        console.log(data[0]);
        console.log(data.length);


        $("#showResults").text("Scrape Results from searching " + processSearch(searchitem)+": ");

        // Fill Table
        for(var i = 0; i < data.length; i++) {
            var tmp = JSON.parse(data[i]);
            $("#Headings").after(
                "<tr>\
                    <td>" + tmp.Name + "</th>\
                    <td>" + tmp.Link + "</th>\
                </tr>"
            );
        }
    });
}


function processSearch(str) {
    str = str.substring(7);
    var a = str.split("%20");
    var ans = "";
    for(var i = 0; i < a.length; i++) {
        ans += a[i] + " ";
    }
    return ans;
}
