# common gateway interface, need to decipher messages from POST request
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# common gateway interface, script is invoked by an HTTP Server, usually to process user input submitted through an HTML
import cgi

# webserver contains two major section handler and main 
# in main will instantaite the server and which port it will listen on
# handler code will determine which code to excecute based on the request sent to the server

# libraries to perform crud operations 
from databasesetup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


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
                # added html form
				output += "<html><body>Hello<form method='POST' enctype='multipart/form-data' action='/hello'> <h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form> " 
				output += "</body></html>"     
				self.wfile.write(output)
				return

			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				# sends a blank line and marks the end of the header
				self.end_headers()

				output = ""
                # added html form
				output += "<html><body>&#161Hola <a href='/hello'>Back to Hello</a><form method='POST' enctype='multipart/form-data' action='/hello'> <h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form> "
            
				# wfile method sends the response back to the client 
				self.wfile.write(output)
				print output
				return
            
		except IOError:
			self.send_error(404, "File not found %s" % self.path)
            
			if self.path.endswith("/restaurants"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				# sends a blank line and marks the end of the header
				self.end_headers()

				output = ""
                output = "<html><body>"
                restaurants = session.query(Restaurant).all()
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "<br>"
                output += "</html></body>"
                self.wfile.write(output)
                print output
                return
            
            
        def do_POST(self):
            try:
                self.send_response(301)
                self.end_headers()
                
                # cgi.parse_header method parses html form header into a main value and dictionary of parameters  
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                
                # to check if form data is being received
                if ctype == 'multipart/form-data':
                    # fields would store all the data in the form
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    # get the value/values for a specific field named "message", will call the field "message when HTML form will be created"
                    messagecontent = fields.get('message')
                    
                    # we have parsed the data given by the user
                    output = ""
                    output += "<html><body>"
                    output += "<h2> Okay, how about this: </h2>"
                    output += "<h1> %s </h1>" % messagecontent[0]
                    output += "</html></body>"
                    self.wfile.write(output)
            except Exception as e:
                print e

			
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
		server.socket.close()
		print "^C entered, stopping the web server"

if __name__ == "__main__":
	main()
