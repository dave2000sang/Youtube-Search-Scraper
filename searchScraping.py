import requests
from bs4 import BeautifulSoup
from csv import writer
import json
import sys


# getLink(search) returns the formated youtube link
def getLink(search):

    strArr = search.split(" ")
    result = ""
    exists = None

    for x in strArr:
        exists = True
        result += x + "+"

    if exists:
        result = result[:-1]

    return "https://www.youtube.com/results?search_query="+result


# localhost HTTP address to receive the search
locallink = "http://localhost:3001/toPython"

# GET request from Node server
r_search = requests.get(locallink)

# Error handling
if r_search.status_code != 200 or r_search.text == '':
    print("Request failed")

else:
    #print (r_search.text)

    search = r_search.text
    link = getLink(search)

    # Scrape the link
    response = requests.get(link)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Select all parts with a href beginning with "/watch?v-" indicating a video link in list
    el = soup.select('a[href^="/watch?v="]')

    # Convert scrape results to JSON
    data = []
    for x in el:
        if x.has_attr('title'):
            name = x.get_text()
            partial_link = x['href']
            full_link = "https://www.youtube.com"+partial_link

            data.append(json.dumps({"Name":name, "Link":full_link}))

    # send data (list of JSON) to server
    print(json.dumps(data))
    sys.stdout.flush()


    '''
    with open('results.csv','w', encoding="utf-8") as csv_file:
        csv_writer = writer(csv_file)
        headers = ['Name', 'Link']
        csv_writer.writerow(headers)

        # Add all findings into .csv file
        for x in el:
            # Filter tags with attribute 'title' (other tags are aria-hidden such as timestamp which is not important)
            if x.has_attr('title'):
                name = x.get_text()
                partial_link = x['href']
                full_link = "https://www.youtube.com"+partial_link
                

                csv_writer.writerow([name, full_link])        # write to csv row
    '''