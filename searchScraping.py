import requests
from bs4 import BeautifulSoup
from csv import writer


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


# Get from Node.js server
r_search = requests.get(locallink)

if r_search == None:
    print ("NULLLL")

# print (response.status_code)

if r_search.status_code != 200 or r_search.text == None:
    print("Request failed")

else:
    print (r_search.text)

    search = r_search.text
    link = getLink(search)
    print (link)

    #link = "https://www.youtube.com/results?search_query=linkin+park"

    response = requests.get(link)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Select all parts with a href beginning with "/watch?v-" indicating a video link
    el = soup.select('a[href^="/watch?v="]')


    with open('results.csv','w') as csv_file:
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
