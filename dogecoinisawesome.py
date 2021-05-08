from flask import Flask, render_template, abort
import markdown

app = Flask(__name__)


@app.route("/")
def homepage():
    try:
        return render_template("index.html")
    except IndexError:
        abort(404)


@app.route("/full-node")
def full_node():
    try:
        readme_file = open("./static/docs/full-node.md", "r")
        md_template_string = markdown.markdown(
            readme_file.read(), extensions=["markdown.extensions.fenced_code"]
        )
        return render_template("full-node.html", markdown_html=md_template_string)
    except IndexError:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("application-error.html"), 404
