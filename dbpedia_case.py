def query(q,epr,f='application/json'):
    try:
        params = {'query': q}
        params = urllib.urlencode(params)
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(epr+'?'+params)
        request.add_header('Accept', f)
        request.get_method = lambda: 'GET'
        url = opener.open(request)
        return url.read()
    except Exception, e:
        traceback.print_exc(file=sys.stdout)
        raise e 

q1 = """
... select ?birthPlace where {
... <http://dbpedia.org/resource/Claude_Monet> <http://dbpedia.org/property/birthPlace> ?birthPlace .
...  }"""
print query(q1,"http://dbpedia.org/sparql")