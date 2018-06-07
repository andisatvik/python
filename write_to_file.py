# Write results to a file

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
  
for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        with open("Real Content.txt","w") as open_file:
            open_file.write("Hello \n")
    

    else: 
        #print(story_heading.contents[0].strip())
        with open("Story_Headings.txt","w") as curr_file:
            curr_file.write(story_heading.contents[0].strip())
