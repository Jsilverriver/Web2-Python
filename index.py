#!/usr/local/bin/python3
print("Content-Type: text/html")  # HTML is following
print()  # blank line, end of headers
import cgi, os, view, html_sanitizer

sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if "id" in form:
    title = pageId = form["id"].value
    description = open("data/" + pageId, "r").read()
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">UPDATE</a>'.format(pageId)
    delete_btn = """
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
        """.format(
        pageId
    )
else:
    title = pageId = "welcome"
    description = "Welcome Page"
    update_link = ""
    delete_btn = ""

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
        {update}
        {delete}
        <h2>{title}</h2>
        <p>{desc}</p>
    </body>
</html>""".format(
        title=title,
        desc=description,
        list=view.getList(),
        update=update_link,
        delete=delete_btn,
    )
)
