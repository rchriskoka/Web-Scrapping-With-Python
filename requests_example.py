#The requests module lets you easily download files from the Web without
#having to worry about complicated issues such as network errors, connection problems and data compression.


import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
#The URL above goes to a text web page for the entire play of Romeo and Juliet provided by Project Gutenberg

print(type(res))
#Check if request succeeded.
if res.status_code == requests.codes.ok:
	print(True)
else:
	print(False)

#Length of the text retrieved.
print(len(res.text))
#We want to see the first 300 characters.
print(res.text[:300])


"""Another way to check for erros is by calling raise_for_status() method on the response object"""
res1 = requests.get('http://inventwithpython.com/page_that_does_not_exist')
