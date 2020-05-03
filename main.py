import sys
from flask import Flask, render_template
from src.api_wikipedia import str_get_wiki_summary

app = Flask(__name__)

@app.route('/')
def home():
    str_wiki_desc = str_get_wiki_summary(str_search="Twelve_Olympians")
    return render_template("index.html", wiki_desc=str_wiki_desc)


@app.route('/<greek_god>')
def profile_page(greek_god):
    str_wiki_desc = str_get_wiki_summary(str_search=greek_god)
    return render_template("profile.html", greek_god=greek_god, wiki_desc=str_wiki_desc)


if __name__ == "__main__":
    app.run(debug=True)