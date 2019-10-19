#!/usr/local/bin/python3
print("Content-Type: text/html")  # HTML is following
print()  # blank line, end of headers
import cgi

form = cgi.FieldStorage()
pageId = form["id"].value
# ?id=HTML과 같이 id값이 나온다. 만약 ID값이 없다면 에러가 나서 페이지에 아무것도 뜨지 않는다. localhost8080/index.py를 입력하면 아무것도 안뜨는 이유.


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
            <li><a href="index.py?id=HTML" >HTML</a></li> 
            <li><a href="index.py?id=CSS" >CSS</a></li> 
            <li><a href="index.py?id=JAVASCRIPT">JAVASCRIPT</a></li> 
        </ol>
            <h2>{title}</h2>

            <p>나의 그리고 우리의 <strong> <u>첫</u> 홈페이지</strong> 가 될것이다. 이것을 계기로 더욱 더 발전해 나가겠지? 후후훗</p>

            <p>
            What is the purpose of a blog?
            There are many reasons for starting a personal blog and only a handful of strong ones for business blogging. Blogging for business, projects, or anything else that might bring you money has a very straightforward purpose – to rank your website higher in Google SERPs, a.k.a. increase your visibility.
            
            As a business, you rely on consumers to keep buying your products and services. As a new business, you rely on blogging to help you get to these consumers and grab their attention. Without blogging, your website would remain invisible, whereas running a blog makes you searchable and competitive.
            
            So, the main purpose of a blog is to connect you to the relevant audience.
            
            Another one is to boost your traffic and send quality leads to your website.
            
            The more frequent and better your blog posts are, the higher the chances for your website to get discovered and visited by your target audience. Which means, a blog is an effective lead generation tool. Add a great call to action (CTA), and it will convert your website traffic into high-quality leads.
            
            But a blog also allows you to showcase your authority and build a brand.
            
            When you use your niche knowledge for creating informative and engaging posts, it builds trust with your audience. Great blogging makes your business looks more credible, which is especially important if your brand is still young and fairly unknown. It ensures presence and authority at the same time.
            </p>
    </body>
</html>""".format(
        title=pageId
    )
)
