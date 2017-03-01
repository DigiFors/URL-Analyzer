#!/usr/bin/env python

import requests
import csv
import sys

def hc_url_analyzer(url):


    crs = open("useragents_alle.txt", "r")

    with open('useragents_alle.txt', "r") as useragents_file:
         user_agent = useragents_file.readlines()
    
    with open ('Results.csv', 'wt') as csvfile:
        fieldnames = ['User-Agent', 'url', "Cache-control", "Server", "Date", "Content-Type", "Transfer-Encoding", "Connection", "Vary", "X-Dropbox-Request-Id", "X-Robots-Tag", "Content-Encoding", 'Strict-Transport-Security', 'pragma', 'x-amz-id-1', 'p3p', 'x-frame-options', 'expires', 'x-ua-compatible', 'Set-cookie', 'Content-Length', 'Cache-Control', 'Location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        for line in user_agent:
        
            headers = {'User-Agent': line.rstrip()}
            r = requests.get(url, headers=headers)
            c = requests.head (url, headers=headers)
            print (r.url)
            incoming_h = r.headers 
            incoming_h['User-Agent'] = line
            incoming_h['url'] = r.url
            incoming_h['Location'] = c.headers ['Location']
                     
            writer.writerow(incoming_h)

try:           
    hc_url_analyzer(sys.argv[1])
except IndexError:
    print ('Usage: hc_url_analyzer http://url') 
    

