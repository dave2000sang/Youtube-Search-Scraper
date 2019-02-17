# Youtube-Search-Scraper
- Scrapes web page on www.youtube.com from user-entered search item and displays video names and links on frontend page
- User enters search item on the web page which is connected to a Node server (by Express web framework) 
and then automatically runs a background python script that uses Beautiful Soup library to scrape the web-site generated from the user input.
- Response returns an array of JSON objects containing the names of all YouTube videos and their corresponding links to frontend site.


## Example Usage:
Here's an example where I input "Linkin Park", telling the program to scrape www.youtube.com with "Linkin Park" in the search bar.

![img](https://github.com/dave2000sang/Youtube-Search-Scraper/blob/master/README%20files/second.png)

- After clicking "Submit" button on the web page, an AJAX call sends "Linkin Park" to a Node server from the app.js script. 
- The server receives this request (using Express API) and calls a Python script, sending "Linkin Park".
- Finally, the python script running beautiful soup library scrapes the YouTube site searching "Linkin Park" and returns an array of JSON objects to the server, which sends it to the frontend client and is displayed in a table.


## Get Started:
- Open local server to "YouTube Search Scraper" directory
- http-server -o
- Run Node server (app.js)
- Voila!

## Future Extensions of Project:
- Automate entire procedure (run everything in background?)     DONE
- Display .csv results onto web page                            DONE (used JSON)
- Beautify front-end web page                                   DONE
- Improve error handling 
- Scrape more than just one page (maybe query user for how many videos to display on .csv)
- Add download links to scraped links
