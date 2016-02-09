#!/usr/bin/python2.7 

import SocketServer
import SimpleHTTPServer


class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler) : # this is a subclass from SimpleHTTPServer.SImpleHttPRequestHanlder

	def do_GET(self) : # this method is a override!
		if self.path == '/admin' :
			self.wfile.write('This page is only for Admins!')
			self.wfile.write(self.headers)

		else :
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


httpServer = SocketServer.TCPServer(("", 10001), HttpRequestHandler)

httpServer.serve_forever()