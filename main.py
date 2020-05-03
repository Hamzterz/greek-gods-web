from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<greek_god>')
def profile_page(greek_god):
    return render_template("profile.html", greek_god=greek_god)


if __name__ == "__main__":
    app.run(debug=True)