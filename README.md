# DogecoinIsAwesome.com
Dogecoin is awesome.

## Running the App Locally

Make sure you have Python 3.9.1 installed locally. You'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```console
$ py -m venv .venv
$ py -m pip install -r requirements.txt
```

### Copy Heroku config vars to your local .env file
The `.env` file lets you capture all the config vars that you need in order to run your app locally.  For each config var that you want to add to your `.env` file, use the following command:

```
$ heroku config -s -a dogecoinisawesome-staging > .env
```

When you start your app using any of the `heroku local` commands, the `.env` file is read, and each name/value pair is inserted into the environment, to mimic the action of config vars.

```console
$ heroku login
$ heroku local web -f Procfile.windows
```

The app should now be running on [localhost:5000](http://localhost:5000/).

## Specifying a Python Runtime and Dependencies 

To specify a Python runtime, add a `runtime.txt` file to your app’s root directory that declares the exact version number to use:

```console
$ cat runtime.txt
python-3.9.0
```

It’s recommended to specify explicit dependency versions in your requirements.txt file. To update this file, you can use the `pip freeze` command in your active virtual environment:

```console
$ py -m pip freeze > requirements.txt
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
- [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)