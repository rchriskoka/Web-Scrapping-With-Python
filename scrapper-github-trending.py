#In this example, we will extract information about the trending repositories such as name, stars,links, etc
# from github.

#Tutorial by Bilguun Batbold.


import requests
from bs4 import BeautifulSoup

#Navigate to the trending page of github and give feedback
page =requests.get('https://github.com/trending')
print(page)
#The above output means that the page was fetched successfully.

#Create a BeautifulSoup object.
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)

#get the repo list
repo = soup.find(class_="repo-list")
