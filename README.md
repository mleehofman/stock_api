Python Project Template
=======
This project is a Python Project Template. It allows you to sttart a new project quickly. 
It has all the necessary settings and packages that allow you to start a new project with all the agreed best practices.


## Main Requirements:

- Python 3.11+
- Pydantic
- PyTest

## Setup:
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

# remove origin
git remote add origin <your_git_url>
```

Git add remote url example (ssh): 

`git remote add origin git@bitbucket.org:logexbv/my-python-project-template-example.git`

### Install requirements
First of all, install and activate virtual environment. It is up to you how (in which way) you do it.

Example: 

- `python3.11 -m venv venv`
- `source venv/bin/activate`

Install packages:

- `pip install poetry`
- `poetry install`
- `pre-commit install`