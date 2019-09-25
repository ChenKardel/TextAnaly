# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchAPI
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

# Replace with your subscription key.
subscription_key = "228f4b3d8e4640e59064122302266549"

# Instantiate the client and replace with your endpoint.
client = WebSearchAPI(CognitiveServicesCredentials(subscription_key), base_url = "https://kardel4.cognitiveservices.azure.com/bing/v7.0")

# Make a request. Replace Yosemite if you'd like.
web_data = client.web.search(query="Congrats to Kirstjen Nielsen, our next Secretary of Homeland Security! Well deserved")
print("\r\nSearched for Query# \" @Breaking911 Build that wall!!👍 \"")

'''
Web pages
If the search response contains web pages, the first result's name and url
are printed.
'''
if hasattr(web_data.web_pages, 'value'):

    print("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))

    for web_page in web_data.web_pages.value:
        print("First web page name: {} ".format(web_page.name))
        print("First web page URL: {} ".format(web_page.url))

else:
    print("Didn't find any web pages...")


'''
News
If the search response contains news, the first result's name and url
are printed.
'''
if hasattr(web_data.news, 'value'):

    print("\r\nNews Results#{}".format(len(web_data.news.value)))

    for news in web_data.news.value:
        print("First News name: {} ".format(news.name))
        print("First News URL: {} ".format(news.url))

else:
    print("Didn't find any news...")

