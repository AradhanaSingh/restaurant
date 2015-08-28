# common gateway interface, need to decipher messages from POST request
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# common gateway interface, script is invoked by an HTTP Server, usually to process user input submitted through an HTML
import cgi

# webserver contains two major section handler and main 
# in main will instantaite the server and which port it will listen on
# handler code will determine which code to excecute based on the request sent to the server

class webserverHandler(BaseHTTPRequestHandler):
	# overrides do_GET method
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				# sends a blank line and marks the end of the header
				self.end_headers()

				output = ""
				output += "<html><body>Hello!"			
				output += "</body></html>"
                
				self.wfile.write(output)
				print output
				return

			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				# sends a blank line and marks the end of the header
				self.end_headers()

				output = ""
				output += "<html><body>&#161Hola <a href='/hello'>Back to Hello</a>"
				
				# wfile method sends the response back to the client 
				self.wfile.write(output)
				print output
				return
		except IOError:
			self.send_error(404, "File not found %s" % self.path)

			
def main():
	try:
		port = 8080
		hostname = ''
		# starts the web server
		# handler is class webServerHandler
		server = HTTPServer((hostname, port), webserverHandler)
		print "Web server running on port %s " % port
		# webserver will run until ^C is hit or when the user exits the application
		server.serve_forever()

	except Exception as e:
		print "^C entered, stopping the web server"
		server.socket.close()

if __name__ == "__main__":
	main()
