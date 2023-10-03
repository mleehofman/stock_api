Python Project Template
=======
This project is a Python Project Template. It allows you to sttart a new project quickly.
It has all the necessary settings and packages that allow you to start a new project with all the agreed best practices.


## Main Requirements/Packages:

- Python 3.11+
- [Pydantic](https://docs.pydantic.dev/latest/) (dataclasses)
- [PyTest](https://docs.pytest.org/en/7.4.x/) (unit tests)
- code format ([black](https://github.com/psf/black), [isort](https://pycqa.github.io/isort/))
- code check ([flake8](https://flake8.pycqa.org/en/latest/), [mypy](https://mypy.readthedocs.io/en/stable/))
- pre-commit

## Setup:
Scenario: you have created a new repository called `example` (`logexbv/example.git`). You want to use a **Python Project Template** for your newly created repo. You created a directory called `example_project` and navigated to the directory (`cd example_project`).

* clone Python Project Template in your new project directory
```bash
# clone template in your current directory
git clone git@bitbucket.org:logexbv/python-project-template.git .
```

### Set a new repo
- Remove existing link to the repo

```bash
# check current remote urls
git remote -v

# remove origin
git remote rm origin
```

- Add a link to a new repo

```bash
# check current remote urls
git remote -v

# add new origin ("example"). Note: example repo doesn't exist.
git remote add origin git@bitbucket.org:logexbv/example.git
```

### Install requirements
First of all, install and activate virtual environment. It is up to you how (in which way) you do it.

Example:

- `python3.11 -m venv venv`
- `source venv/bin/activate`

Install packages:

- `pip install poetry`
- `poetry install`
- `pre-commit install`

## Development
Remove or edit/update files:
- `src/main_app_template.py`
- `tests/test_template.py`

Now you are ready to develop your new project! Dont forget to update your **README.md** file accordingly.
