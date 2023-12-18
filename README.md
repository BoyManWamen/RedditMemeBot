<h1 align="center"> 
   <span>RedditMemeBot</span>
</h1>

<div align="center">

<a href="https://github.com/BoyManWamen/RedditMemeBot/stargazers">![GitHub Repo stars](https://img.shields.io/github/stars/BoyManWamen/RedditMemeBot?style=social)</a>
<a href="https://github-com.translate.goog/BoyManWamen/RedditMemeBot/blob/main/README.md?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp">![Translate](https://img.shields.io/badge/Translate-blue)</a>
</div>

<div align="center">
<img src="https://media.giphy.com/media/xT8qB4foF1nxHZwpLa/giphy.gif"/>
</div>

## Table of Contents

* [Description](#description)
* [Dependencies](#dependencies)
* [Installing](#installing)
* [Executing](#executing-program)
* [Authors](#authors)
* [Version History](#version-history)
* [License](#license)

## Description

Automate your daily dose of humor with the RedditMemeBot! This Python-based bot is designed to effortlessly curate and post memes to your favorite subreddits, adding a touch of joy to your online experience. Forget the manual search for amusing content – let RedditMemeBot handle it for you.

## Getting Started

### Dependencies

The list of dependencies for this Reddit bot is the following:

```praw```:

Description: Python Reddit API Wrapper
Version: 7.7.1

```icrawler```:

Description: A flexible and powerful image crawler library
Version: 0.6.7

### Installing

Move into the project directory.

```sh
cd RedditMemeBot
```

Make sure you have installed all of the dependencies such as GoogleImageCrawler and praw.

```sh
pip install icrawler praw
```

Next, make sure that you change ```CLIENT_ID```, ```SECRET```, ```PASSWORD```, and ```USERNAME``` in the following lines of code:

```py
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("SECRET"),
    password=os.getenv("PASSWORD"),
    user_agent="Reddit Image Poster by u/",
    username=os.getenv("USERNAME"),
)
```

In order to get your client id and client secret, you must work with Reddit OAuth. The documentation for how is linked below.

[Praw Documentation](https://praw.readthedocs.io/en/stable/)

Make sure to change ```me_irl``` in the following lines of code to choose which subreddit you want to upload your memes to.

```py
reddit.subreddit("me_irl").submit_image("me_irl", f"./dataset/{randomword} meme/{file}")
```

### Executing Program

In order to run the program, you can use the following command in the terminal.

```sh
python src\main.py
```

## Authors

Huy Hoang

## Version History

* 1.0.0
    * Initial Release

## License

This project is licensed under the MIT License
