WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import SimpleHTTPServer
import SocketServer

class WebHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    # Disable logging DNS lookups
    def address_string(self):
        return str(self.client_address[0])


PORT = 80

Handler = WebHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "httpd serving at port", PORT
httpd.serve_forever()
