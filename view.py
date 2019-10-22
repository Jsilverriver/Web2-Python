import os, html_sanitizer


def getList():
    files = os.listdir("data")
    sanitizer = html_sanitizer.Sanitizer()
    web_list = ""
    for item in files:
        item = sanitizer.sanitize(item)
        web_list = (
            web_list
            + '<li><a href="index.py?id={name}" >{name}</a></li>'.format(name=item)
        )
    return web_list
