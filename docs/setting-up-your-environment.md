## Setting Up Your Environment

#### Build The Site Locally

DogecoinIsAwesome.com is created using [Python
Flask](https://flask.palletsprojects.com/en/1.1.x/). To build the site, you
need to go through a one-time installation procedure that takes 10 to 20
minutes. After that you can build the site an unlimited number of times with no
extra work.

**Create A Python Virtual Environment**

Make sure you have Python 3.9.5 installed locally and check out the site repository.

To create a Python virtual environment, simply run this command in the top-level
directory of your local repository:

    py -m venv .venv

And install the necessary dependencies using `pip`:

    py -m pip install -r requirements.txt

**Setup Config Vars**

Create a `.env` file in the the top-level of your local repository and then copy and
paste the following lines into the file:

    FLASK_APP=dogecoinisawesome.py
    FLASK_ENV=development

**Preview The Site**

To preview the website in your local browser, run the following command:

    py -m flask run

This will compile the site and then print a message like this:

```
* Serving Flask app "dogecoinisawesome.py" (lazy loading)
* Environment: development
* Debug mode: on
* Restarting with stat
* Debugger is active!
* Debugger PIN: 137-255-289
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Visit the indicated URL in your browser to view the site.
