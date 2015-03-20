#!/usr/bin/env python3
###
# (C) Copyright 2014 Wookieware    www.wookieware.com
# R. Kauffman
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###
import sys
import cgi
import cgitb; cgitb.enable()

def getform():
  form = cgi.FieldStorage()
  host = form.getvalue('server')
  user = form.getvalue('user')
  passwd = form.getvalue('passwd')
  return (server, user, passwd)
  
def printpage(pagevar1, pagevar2, pagevar3):
  """
  pagevar1 = Header/Title
  pagevar2 = Subtitle
  pagevar3 = Description text
  """
  print ("Content-type:text/html\r\n\r\n")
  print ("<!DOCTYPE html>")
  print ("<html>")
  print ("<head>")
  print ("<title> Docker Lamp</title>")
  print ("<link rel=\"stylesheet\" type\"text/css\" href=\"../../styles/tasks.css\"/>")
  print ("<script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js\"></script>")
  print ("</head>")
  print ("<body>")
  print ("<header>")
  print ("<h1>  {} </h1>".format(pagevar1))
  print ("</header>") 
  print ("<h3> {} </h3>".format(pagevar2))
  print ("<p> {} </p>".format(pagevar3))
  print ("<hr>")
  print ("<br>")


def pagetail():
  print ("</section>")
  print ("</main>")
  print ("<footer>")
  print ("<a href=\"/getxapi2.html\">Home</a>")
  print ("<center><font face=\"Arial\" size=\"1\"API Solutions From WookieWare 2014</font></center>")
  print ("</footer>")
  print ("</body>")
  print ("</html>")

def pager():
    pagevar1 = "Python LAMP Test"
    pagevar2 = "Sample text goes here"
    pagevar3 = "You can add additional information to the page by editing this text"
    printpage(pagevar1, pagevar2, pagevar3)


def main():
    # Arguments supplied from getform function
    server, user, passwd = getform()
    
    #server = "10.132.0.10"
    #user = "xod442"
    #passwd = "RoseBud"
    
        
    pager()
    print ("<main>")
    print ("<section id=\"mainReturn\">")
    print ("The server Ip address:{} ".format(server))
    print ("The username:{} ".format(user))
    print ("The password:{} ".format(passwd))
    pagetail()

   
if __name__ == '__main__':
    sys.exit(main())

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
