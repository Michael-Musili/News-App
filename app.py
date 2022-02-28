from flask import Flask,render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def home():
    newsapi = NewsApiClient(api_key="83f8de393be94ef8ad50bd4517fb123f")
    top_headlines=newsapi.get_top_headlines(source="bbc news")

    t_article = top_headlines["articles"]

    #list of content

    news = []
    desc = []
    img = []
    p_date = []
    url = []

    #fetch articles
    for i in range(len(t_article)):
        main_article = t_article[i]
        

        news.append(main_article["title"])
        desc.append(main_article["description"])
        img.append(main_article["urlToImage"])
        p_date.append(main_article["publishedAt"])
        url.append(main_article["url"])

        
        contents =zip(news,desc, img ,p_date,url)
#
    return render_template("home.html" ,contents=contents)
    

if __name__ ==" _main_ ":
    app.run(debug=True)