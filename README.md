# Newspaper3k Wrapper
Wraps over newspaper3k library to provide support to nepali sites

# Current State
* Works for majority of nepali news site
* Tested site list is given in sites.txt
* Currently only title and text field is guarenteed to have data. 

# Installation
```
$ git clone https://github.com/pykancha/newspaper3k_wrapper
$ pip install .
```

## Use as dependency
In your requirements.txt file add;
```
-e git+https://github.com/pykancha/newspaper3k_wrapper.git
```

### Alternatively if you use pyproject.toml file
```
newspaper3k_wrapper = { git = "https://github.com/pykancha/newspaper3k_wrapper.git" }
```

# Usage and Installation Problems
Please visit [newpaper3k](https://pypi.org/project/newspaper3k) for any usage or installation help.

```
from newspaper_wrapper import Article

url = 'https://www.himalkhabar.com/news/113640'
article = Article(url, language='hi')

article.download()
article.parse()
article.nlp()

print(article.title, article.text)
```
