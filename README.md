# Youtube-Search-Scraper


- YouTube search scraper from www.youtube.com. 
- User enters search item on the web page (running on localhost) which is connected to a node.js server (by Express API) 
and then POST requests a background python script that finally scrapes the web-site generated from the user input.
- Outputs a .csv file containing Names of all YouTube videos and their corresponding links


## Future Extensions of Project:
- Automate entire procedure (run everything in background?)
- Display .csv results onto web page
- Beautify front-end web page
- Improve error handling
- Add download links to scraped links


## Example Usage:
Here's an example where I input "Linkin Park", telling the program to scrape www.youtube.com with "Linkin Park" in the search bar.

![img](https://github.com/dave2000sang/Youtube-Search-Scraper/blob/master/README%20files/ExampleWebPage.png)

- After clicking "Submit" button on the web page, it sends "Linkin Park" to a node.js server from the app.js script through a POST
request. 
- The server receives this request (using Express module) and sends "Linkin Park" to the python script running in the background
through a different POST request running on a different port number.
- Finally, the python script runs and outputs this lovely .csv file

![img2](https://github.com/dave2000sang/Youtube-Search-Scraper/blob/master/README%20files/LinkinParkCSV.PNG)
