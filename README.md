# Mattos Lab Site

This is the repository for building the Mattos Lab site generator.

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
