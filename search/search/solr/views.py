from django.shortcuts import render

from solr.classes.SearchHandler import SearchHandler
# Create your views here.
def home(request):
    
    context = {'page': 'Solr Search'}
    return render(request, 'solr/index.html', context)
def search(request):
        solrServerUrl="http://localhost:8983/solr/solrTest/select"
        queryStr = request.GET["q"]
        
          # queryStr = '"' + queryStr + '"'

        # Make the connection with Solr and get the reposnse to the query
        params = {
        'q':'"' + queryStr + '"',
        'df' : 'text',
        'fl' : 'text, id',
        'wt':'json',
        'indent' : 'on',
        'hl':'on',
            'hl.fl':'content',
            'hl.simple.pre':'<em>',
            'hl.simple.post':'</em>',
            'hl.snippets':20,
            'hl.fragsize':200,
            'hl.maxAnalyzedChars':100000,
        #'facet':'on',
            #'facet.field':'content'
            #'debugQuery':'true'
        }
    
        sh=SearchHandler()
        searchResult=sh.solrSearch(solrServerUrl, params)
        responseTime=(searchResult["responseHeader"]["QTime"]/1000)%60
        context = {'queryStr':queryStr,'searchResult': searchResult,'responseTime':responseTime}
        return render(request, 'solr/search.html', context)
    
def landing(request):
        solrServerUrl="http://localhost:8983/solr/solrTest/get"
        queryStr = request.GET["id"]
        
        print (queryStr)
          # queryStr = '"' + queryStr + '"'

        # Make the connection with Solr and get the reposnse to the query
        params = {
        'id': queryStr
        
      
        }
    
        sh=SearchHandler()
        searchResult=sh.solrSearch(solrServerUrl, params)
       
        context = {'searchResult': searchResult}
        return render(request, 'solr/landing.html', context)

