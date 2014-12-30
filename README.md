# Mattos Lab Site

Static site generator for the Mattos Lab site

The idea is that you can edit some .yml files that contain the content
and then run `python make.py`, and the finished html files, css, images, etc.
will appear under the `build/` directory.

## Setting up a develpoment environment

To make edits and test on your computer, make sure you have the following installed:

- git (run `which git` to see if installed)
- virtualenv (run `which virtualenv` to see if installed)
- virtualenvwrapper (run `which mkvirtualenv` to see if installed)

Then run the following commands:

```bash
$ git clone <this repo>
$ cd mattoslabsite
$ mkvirtualenv mattoslabsite
$ pip install -r requirements.txt
```

To re-enter the python virtual environment the next time run

```bash
$ workon mattoslabsite
```

To build the site run

```bash
$ python make.py
```

To server the files (just locally to yourself) and test the website, run

```bash
$ python -m SimpleHTTPServer 4444
```

and navigate your browser to http://localhost:4444/build/home.html.
