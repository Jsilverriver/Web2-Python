#!/usr/local/bin/python3
print("Content-Type: text/html")  # HTML is following
print()  # blank line, end of headers
print("Hello World")
print(
    """<!DOCTYPE html>
<html>
    <head>   
        <title>Develope myself - welcome</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="style.css">
        <script src="colors.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="colors.js"></script>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-146579754-1"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'UA-146579754-1');
        </script>   
    </head>`

    <body>
            <p>
                    <!--Start of Tawk.to Script-->
                    <script type="text/javascript">
                    var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
                    (function(){
                    var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
                    s1.async=true;
                    s1.src='https://embed.tawk.to/5d665c6c77aa790be33127bc/default';
                    s1.charset='UTF-8';
                    s1.setAttribute('crossorigin','*');
                    s0.parentNode.insertBefore(s1,s0);
                    })();
                    </script>
                    <!--End of Tawk.to Script-->
            
            </p>


        <h1><a href="index.html">요를레히호</a></h1>
        
        <input type="button" value="night" onclick="
        nightDayHandler(this);
        ">

    <div id="grid">
        <ol>
            <li><a href="1.html" >Coding</a></li> 
            <li><a href="2.html" >workout</a></li> 
            <li><a href="3.html">Allofmylove</a></li> 
        </ol>

        <!-- 태그를 그 의도에 맞게 만드는 것이 중요하다. 왜냐하면 그것이 의미가 없어질수 있기 때문에, 그리고 accessibility라는 개념을 알자-->
        <div id="blogArticle">
            <h2>blog</h2>

            <p>나의 그리고 우리의 <strong> <u>첫</u> 홈페이지</strong> 가 될것이다. 이것을 계기로 더욱 더 발전해 나가겠지? 후후훗</p>

            <!--br태그와 p태그의 차이. 올바른 점. 그리고 p태그는 한번만 떨어트릴수 있는 단점이 있기는 하지만 우리에겐 css가 있다!-->
            <p style="margin-top:40px">
            What is a Blog?
            Definition of blog
            A blog (shortening of “weblog”) is an online journal or informational website displaying information in the reverse chronological order, with latest posts appearing first. It is a platform where a writer or even a group of writers share their views on an individual subject.
            </p>

            <!--src=source-->
            <!--이미지파일은 unsplash에서 가져옴-->
            <!--with,src 등을 'attribute' 속성이라고 말한다. 그리고 그것의 위치는 바뀌어도 상관없다.-->
            <img src ="blogpic.jpg" width="500px" ><br>
            <a href="https://unsplash.com/" target="_blanck" title="make new tap where the image you can get">blogimagewebsite</a>

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
        </div>
    </div>
  

    ">
        <p>
            <div id="disqus_thread"></div>
            <script>

            /**
            *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
            *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
            /*
            var disqus_config = function () {
            this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
            this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
            };
            */
            (function() { // DON'T EDIT BELOW THIS LINE
            var d = document, s = d.createElement('script');
            s.src = 'https://web-1-exp7k9porz.disqus.com/embed.js';
            s.setAttribute('data-timestamp', +new Date());
            (d.head || d.body).appendChild(s);
            })();
            </script>
            <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
                                        
        </p>
    </body>
</html>"""
)
