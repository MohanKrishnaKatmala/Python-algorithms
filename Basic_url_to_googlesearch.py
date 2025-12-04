"""
Give the url creation of the google to search a query of the python tutorial.
Output:
Give the url of the python tutorial of the google search.
"""
from urllib.parse import urlencode,urlunparse
scheme="https"
net_location="www.google.com"
path="search"
query=urlencode({"q":"python tutorial"})
build_url=urlunparse((scheme,net_location,path,"",query,""))
print("builded url :",build_url)
