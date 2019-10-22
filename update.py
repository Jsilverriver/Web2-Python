#!/usr/local/bin/python3
print("Content-Type: text/html")  # HTML is following
print()  # blank line, end of headers
import cgi, os, view


form = cgi.FieldStorage()
if "id" in form:
    pageId = form["id"].value
    description = open("data/" + pageId, "r").read()
else:
    pageId = "welcome"
    description = "Welcome Page"

print(
    """<!DOCTYPE html>
<html>
    <head>   
        <title>web1 - welcome</title>
        <meta charset="utf-8">
    </head>

    <body>
        <h1><a href="index.py">요를레히호</a></h1>

        <ol>
            {list}
        </ol>

        <a href="create.py">CREATE</a>
        <form action="process_update.py" method="post">
            <input type="hidden" name="pageId" value= "{default_updated_title}"> 
            <p><input type="text" name="title" placeholder="title" value={default_updated_title}></p>
            <p><textarea rows="4" name="description" placeholder="description">{default_updated_desc}</textarea></p>
            <p><input type="submit"></P>
        </form>
    </body>
</html>""".format(
        title=pageId,
        desc=description,
        list=view.getList(),
        default_updated_title=pageId,
        default_updated_desc=description,
    )
)
