from bottle import template
import P4_module
import webbrowser

sentence = P4_module.article()
sentence = sentence.split("\n")
# remove auther 
del sentence[0]


def Generate_html(inputs):
    template_demo="""
    <html>
    <head>
    </head>
    <body>
    % import random
    % sentence = random.choice(items)
    <h2>{{sentence}}</h2>
    %end
    </body
    </html>
    """
    
    html = template(template_demo,items=inputs)
    
    with open("test.html",'wb') as f:
        f.write(html.encode('utf-8'))


Generate_html(sentence)
webbrowser.open("test.html")



















