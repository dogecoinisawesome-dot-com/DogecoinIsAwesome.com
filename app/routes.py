import markdown
from flask import abort, render_template

from app import app


@app.route("/")
@app.route("/index")
def homepage():
    try:
        return render_template("index.html", title="Home")
    except IndexError:
        abort(404)


@app.route("/full-node")
def full_node():
    try:
        readme_file = open("./app/static/docs/full-node.md", "r")
        md_template_string = markdown.markdown(
            readme_file.read(),
            extensions=["markdown.extensions.fenced_code", "markdown.extensions.toc"],
        )
        return render_template(
            "full-node.html",
            title="Running a Full Node",
            markdown_html=md_template_string,
        )
    except IndexError:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
