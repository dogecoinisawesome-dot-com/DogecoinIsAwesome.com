import markdown
from flask import abort, render_template

from app import app

#
# Main pages.
#
@app.route("/")
@app.route("/index")
def homepage():
    try:
        return render_template("index.html", title="Home")
    except IndexError:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


#
# Guides.
#
@app.route("/dogecoin-wallets")
def wallets():
    try:
        readme_file = open("./app/static/docs/dogecoin-wallets.md", "r")
        md_template_string = markdown.markdown(
            readme_file.read(),
            extensions=[
                "markdown.extensions.fenced_code",
                "markdown.extensions.toc",
                "markdown.extensions.footnotes",
            ],
        )
        return render_template(
            "content.html",
            title="Which wallet is best for Dogecoin?",
            markdown_html=md_template_string,
        )
    except IndexError:
        abort(404)


@app.route("/faq")
def faq():
    try:
        readme_file = open("./app/static/docs/faq.md", "r")
        md_template_string = markdown.markdown(
            readme_file.read(),
            extensions=[
                "markdown.extensions.fenced_code",
                "markdown.extensions.toc",
                "markdown.extensions.footnotes",
            ],
        )
        return render_template(
            "content.html",
            title="Frequently Asked Questions and Myths About Dogecoin",
            markdown_html=md_template_string,
        )
    except IndexError:
        abort(404)


@app.route("/full-node")
def full_node():
    try:
        readme_file = open("./app/static/docs/full-node.md", "r")
        md_template_string = markdown.markdown(
            readme_file.read(),
            extensions=[
                "markdown.extensions.fenced_code",
                "markdown.extensions.toc",
                "markdown.extensions.footnotes",
            ],
        )
        return render_template(
            "content.html",
            title="Running a Full Node",
            markdown_html=md_template_string,
        )
    except IndexError:
        abort(404)
