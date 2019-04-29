import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = "https://www.cnblogs.com/"
params = {
    "CategoryType": "SiteHome", 
    "ParentCategoryId": 0, 
    "CategoryId": 808,
    "PageIndex": 2, 
    "TotalPostCount": 4000, 
    "ItemListActionName": "PostList"
}

def get_url(pageIdx):
    global url
    global params
    params['PageIndex'] = pageIdx
    query_string = urllib.parse.urlencode(params)
    url1 = url + '?' + query_string
    with urllib.request.urlopen( url1 ) as response:
        response_text = response.read()
        soup = BeautifulSoup(response_text)
        for tag in soup.select(".titlelnk"):
            print(tag.contents)
        print('\n')

for pageIdx in range(1, 3):
    get_url(pageIdx)