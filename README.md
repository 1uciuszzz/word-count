# word-count

counting all the same word in an article.

# description

this project is unfinished.

# usage

make sure you have install pipenv glabally, if not, you should run

```bash
pip install pipenv
```

now run this command in your terminal here:

```bash
pipenv install
```

```bash
pipenv run python app.py <text file you want to count> <file you had known words> <result file>
```

example:

```bash
pipenv run python app.py document.md known_words.json result.md
```

# configuration

open `app.py` and modify line 7

open `known_words.json` file and append word you want to ignore to data list.
