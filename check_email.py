#!/usr/bin/python3

import urllib.request
import json

def check_email(url, list_domain):
    result = {}
    try:
        #try open url
        response = urllib.request.urlopen(url)
        #read and decode data
        data = response.read()
        text = data.decode('utf-8')
        #convert with json
        json_array = json.loads(text)
        #parsing list
        for one_array in range(len(json_array)):
            if json_array[one_array]['email'].split('.')[-1] in list_domain:
                result[json_array[one_array]['name']] = json_array[one_array]['email']
        print(result)
        return result
    #if url is not available return 0
    except urllib.error.URLError:
        print(('Urlopen error: {} connection refused').format(url))
        return 0

#do script by default
if __name__ == "__main__":
    url = 'http://jsonplaceholder.typicode.com/users'
    list_domain = {'net', 'org'}
    check_email(url, list_domain)

