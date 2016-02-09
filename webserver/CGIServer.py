#!/usr/bin/python3

#This has to be run with python3!!

from http.server import CGIHTTPRequestHandler, HTTPServer

handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin', '/htbin']  # this is where the cgi files 
server = HTTPServer(("", 10000), handler)
server.serve_forever()