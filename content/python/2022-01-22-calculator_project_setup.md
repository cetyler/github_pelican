Title: Calculator Project -- Setup
Date: 2022-01-22 15:00
Category: Python
Tags: python, project, library, package
Author: Christopher
Summary: Initial setup of the calculator project.
comment_id: calculator_setup
Status: draft

## Overview

From the previous article, the plan is to create
[calculator](https://github.com/cetyler/calculator) in order to update my
Python workflow.
This article will cover setting up the project.

## Automating Initial Setup

Will use a Makefile to help automate creating the Python virtual environment
and to install [flit](https://flit.readthedocs.io/en/latest/).
[Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) template that I
plan to create will include `requirements-develop.txt` and
`requirement-doc.txt` to install packages to help create the Python package.
The developer will need to edit both requirement files to add/remove packages
and/or set package versions.

The main downside to using a Makefile will be how to use it in Windows.
Unfortunately, at work I use Windows 10 to do some of my programming.
I should be able to [GNU Make](https://www.gnu.org/software/make/) but that
will be tested later.

Using `make setup` should do the following:

- Create `venv` virtual environment.
- Upgrade pip.
- Install flit and run `flit init`.

## Cookiecutter

My plan is to create my Cookiecutter template at the end.
The template should include the following:

- MakeFile.
- Requirement files.
- README.md
- Folders.
  - Tests.
  - Project folder (ex. calculator).
  - Docs.
- Helper files like .gitignore, pre-commit, .flake8, mypy.ini, etc.
- **Optional:** pyproject.toml
  - That way it can be setup without running `flit init`.

The questions will help fill in the information required for the files that
will be added.
Cookiecutter should work with either a package or a library.

## Documentation

Documentation will be at minimum in two parts -- for the package/library and
for the developer of that package/library.

### Developer

At minimum there will be a `README.md` that will describe how to install the
package and some basic information on how to use the package.
It can also be used for user information if they are more technical (ex.
Github).

Mote detailed documentation will use `sphinx` and will also include any APIs.
Developer documentation will not be included with the package through `pip
install`.

I will also use a wiki (Gitea/Github/Gitlab) depending on the project.

### User

At minimum will have `GettingStarted.md` if the program is simple enough.
Help should be in the program (beyond how to install the program).
Will use `sphinx` when more lengthy documentation is required.
That documentation will be included in the package and ideally hosted at a
website if publicly shared.

## Calculator Setup

Basically above was documented as I created the calculator repo.

