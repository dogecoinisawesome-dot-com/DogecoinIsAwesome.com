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
            title="Choose a Dogecoin Wallet",
            description="Once you own Dogecoin, storing it safely and securely is important. Learn more about the recommended wallets and storage solutions.",
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
            title="Frequently Asked Questions",
            description="To learn more about Dogecoin, take a look at our FAQs.",
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
            title="Running A Dogecoin Full Node",
            description="Support the Dogecoin network by running your own full node.",
            markdown_html=md_template_string,
        )
    except IndexError:
        abort(404)


@app.route("/full-node-raspberry-pi")
def full_node_raspberry_pi():
    try:
        readme_file = open("./app/static/docs/full-node-raspberry-pi.md", "r")
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
            title="Raspberry Pi Full Node Setup",
            description="Run a Dogecoin full node on a Raspberry Pi.",
            markdown_html=md_template_string,
        )
    except IndexError:
        abort(404)
