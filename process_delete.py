#!/usr/local/bin/python3

# print("Content-Type: text/html")  # HTML is following
# print()  # blank line, end of headers

import cgi, os

form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove("data/" + pageId)

# Redirection
print("Location: index.py")
print()
