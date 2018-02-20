from urllib.parse import urlencode # python 3
import json
import requests
#Generally, simplejson module is more up-to-date and faster than the built-in jason module
# http://stackoverflow.com/questions/712791/what-are-the-differences-between-json-and-simplejson-python-modules


class SearchHandler:
  
    
   def solrSearch(self,solrServerUrl,params):
       

        # Make the connection with Solr and get the reposnse to the query
       
        data = urlencode(params).encode()
        response=requests.get(solrServerUrl, data=params)
        json_data = json.loads(response.text)
       # print(json_data["highlighting"])
        return json_data