Newspaper3k Wrapper: Nepali Article scraping & curation
========================================

![Tests](https://github.com/pykancha/newspaper3k_wrapper/workflows/Tests/badge.svg?branch=master)


# Newspaper3k Wrapper
A Wrapper over newspaper3k library to provide support to nepali sites

# Current State
* Works for majority of nepali news site
* Tested site list is given in sites.txt
* Currently only title and text field is guarenteed to have data. 

# Installation
In case you run in some troubles during installation performing the steps below,
Visit [newpaper3k](https://github.com/codelucas/newspaper) for detail usage/installation help.

```
$ git clone https://github.com/pykancha/newspaper3k_wrapper.git
$ pip install -r requirements.txt
$ python setup.py install 
$ python download_corpora.py
```

## Use as dependency
Once you have run ```python download_corpora.py``` command on your machine,
you can use:
```
python -m pip install git+https://github.com/pykancha/newspaper3k_wrapper.git#egg=newspaper_wrapper
```
to simply install it as regular package without cloning repo to your folder.

### To specify this git dependency for your project,
In your requirements.txt file add;
```
-e git+https://github.com/pykancha/newspaper3k_wrapper.git#egg=newspaper_wrapper
```

### Alternatively if you use Poetry
Use the command
```
poetry add git+https://github.com/pykancha/newspaper3k_wrapper.git
```
Alternatively, edit in your pyproject.toml file
```
newspaper3k_wrapper = { git = "https://github.com/pykancha/newspaper3k_wrapper.git" }
```

# Sample Usage

```
>> from newspaper_wrapper import Article

>> url = 'https://www.himalkhabar.com/news/113640'
>> article = Article(url, language='hi')
>> article.download()

>>> article.html
'<!DOCTYPE HTML><html itemscope itemtype="http://...'

>> article.parse()
>> article.nlp()

>> print(article.title, article.text)
```

# Development
Refer to: [Docs - Adding new languages](https://newspaper.readthedocs.io/en/latest/user_guide/advanced.html#adding-new-languages)

```
$ git clone https://github.com/pykancha/newspaper3k_wrapper
$ cd newspaper3k_wrapper
$ python -m pip install -e .
$ python download_corpora.py
```

Make changes and run the tests
```
$ python tests/unit_tests.py 
$ python tests/unit_tests.py fulltext
```

