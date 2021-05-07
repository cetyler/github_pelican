Title: Switch Website to Pelican
Date: 2021-04-10 14:30
Category: Blog
Tags: website, pelican, jekyll
Author: Christopher
Summary: Switch from Jekyll to Pelican.
Status: published

## Why I Changed

My initial website was done using the default for GitHub Pages using Jekyll.
Jekyll would probably have been fine but I knew that I wanted to use Jupyter
Notebooks.
Also I know Python a lot more than Ruby so I thought it made sense to make the
change sooner rather than waiting until I have problems with different kinds of
content.

## Changing to Pelican

Initially I used
[Justin Naldzin](https://justinnaldzin.github.io/create-a-website-using-github-pages-and-pelican.html)
blog post but it was not up to date but was a good start.
I then went to [Pelican](https://blog.getpelican.com/) and used a combo of both
to get up and going.
After getting the theme to work and trying some test pages, I moved the handful
of my posts and was able to get things to work using `make devserver` and
viewing my website locally.
I did had to add in `pelicanconf.py` the option `BIND = ''` so that I could see
my website on my local network as I work on a remote VM.

## Updating My GitHub Page

First I open `MakeFile` and do the following:

    ONELEVELUPDIR = $(subst $(notdir $(CURDIR)),,$(CURDIR))
    OUTPUTDIR = $(ONELEVELUPDIR)/github_page

I did this instead of doing a git submodule but I may change that later.

Also I set `DELETE_OUTPUT_DIRECTORY` to `False`.
Finally I run `make publish` to publish my website and commit that to master on
my GitHub page repo.

## Conclusion

I now have my website to the same level as I had using Jekyll.
Later I will add and verify using Jupyter Notebooks.