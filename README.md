# stocks_api
stock_api
A python program to get information about stocks

***This program makes use of the fmpsdk library and the
financial modeling prep: https://site.financialmodelingprep.com/***
<<<<<<< HEAD
=======

*Please keep this repo up-to-date. Don't hesitate to create Merge Requests with proposed changes/updates.*
>>>>>>> a4dc2e3 (improve_read_me_file)


## Main requirements/packages:

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

# add new origin ("example"). Note: "example" repo doesn't exist in Logex the bitbucket. It is used as example.
git remote add origin git@bitbucket.org:logexbv/example.git
```

### Install requirements
First of all, install and activate virtual environment. It is up to you how (in which way) you do it.

Example:

- `python3.11 -m venv venv`
- `source venv/bin/activate`

Install packages:

- `pip install poetry=="1.6.1"`. Install fixed version to avoid including breaking changes
- `poetry install`
- `pre-commit install`

## Development
Remove or edit/update files:

- `src/main_app_template.py`
- `tests/test_template.py`

Now you are ready to develop your new project! Dont forget to update your **README.md** file accordingly.

### Pipelines

Bitbucket pipelines are configured to run Quality Checks and Unit Tests using the `Python 3.11` on all Pull Requests and on the `main` branch. Keep in mind to change the image name and all the occurencies of `python-project-template`.

### Tests

- `poetry run pytest tests/` or `pytest tests/`


## Troubleshooting

In case you have issues with running Python commands:

- use `poetry run python <some command>` instead of `python <some command>`. [Docs](https://python-poetry.org/docs/basic-usage/#using-poetry-run)

Tests:

- In order to debug tests and using breakpoints (in tests) you need to run tests with `--no-cov` argument
