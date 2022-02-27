# **Setting Up Your Environment**

## **Build The Site Locally**

DogecoinIsAwesome.com is created using [Python
Flask](https://flask.palletsprojects.com/en/1.1.x/).

To build the site, you
need to go through a one-time installation procedure that takes 5 to 10
minutes.

After that you can build the site an unlimited number of times with no
extra work.

### **Create A Python Virtual Environment**

Make sure you have Python 3.10.2 installed locally and check out the site repository.

To create a Python virtual environment, simply run this command in the top-level
directory of your local repository:

    py -m venv .venv

And install the necessary dependencies using `pip`:

    py -m pip install -r requirements.txt

### **Preview The Site**

1.  Download and install the latest version of [Docker Desktop](https://docs.docker.com/get-docker/).

1.  To start the application, run the following command:

        docker-compose -f docker-compose.dev.yml up --build

1.  To preview the website in your local browser, go to: [http://localhost:8000/](http://localhost:8000/)

1.  Press ctrl-c to stop the container.
