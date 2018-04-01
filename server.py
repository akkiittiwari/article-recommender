from flask import Flask, render_template
from doc2vec import *
import sys

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    return render_template('articles.html',
        articles=articles
        )


@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    filtered_article = []
    for art in articles:
        if((topic +'/' + filename) in art[0]):
            filtered_article = art
    articles_filtered = [a for a in articles if a != filtered_article]
    recommeded_art = recommended(filtered_article, articles_filtered, 5)
    return render_template('article.html',
                           title=filtered_article[1],
                           main_art=filtered_article[2],
                           articles=recommeded_art
                           )


# initialization

i = sys.argv.index('server:app')
glove_filename = sys.argv[i+1]
articles_dirname = sys.argv[i+2]

gloves = load_glove(glove_filename)
articles = load_articles(articles_dirname, gloves)

