# EDs Finance
A website where users can create an account to manage a fictional portfolio of stocks of their choice. It can be a fun way for users to practice and gain experience buying and selling assets that reflect real world prices without risk.

## Overview
EDs Finance web app built with Python using the Flask framework and a SQLite database. I used bootstrap design the style of my site and Jinja to help generate and format the tables presented on it. 

### The Website
If you haven't already logged in, you will be redirected to the login page where you can either login or signup. When users create an account, they are given $10,000 fake cash as a welcome bonus to purchase stocks. Lucky you! In order to research stock prices before trading, you may use the quote page to search stocks to get a price quote. Once you are ready to make a trade, you can use the buy page to purchase new stocks or the sell page to sell stocks you already own. The history page will give a record of all your transactions while the home gives a breakdown of your current holdings and cash.

### Getting Started
In order to use this website you must first serve this app. First you must first clone this reposity. Then to create a virtual environment use 'python3 -m venv .venv' and install dependencies with 'pip install -r requirements.txt'. Next use the command 'export FLASK_APP=application.py' in order to set the flask environment variable. In order to use real life stock prices you will need to follow the instructions at [CS50s project page](https://cs50.harvard.edu/x/2022/psets/9/finance/#configuring) and create an account at [IEX](https://www.iexexchange.io/). Please see the [Notes](#notes) as I have changed my app in order to no longer require this setup. Finally, run the command 'flask run'.

### Notes
I created this project as part of the [Harvard CS50s Introduction to Computer Science](https://cs50.harvard.edu/x/2023/) course. My site originally used an API request to check current stock prices on [IEX](https://www.iexexchange.io/). In order for this to work you needed to create a trial account and add your token as an environment variable. In order to demonstrate how the site works without requiring you to create an IEX account I have temporarily commented out the original lookup function located in helpers.py. The lookup function currently only returns made up prices for the stock symbols AAAA, BBBB, CCCC and DDDD. You will still need to create an environment variable by excuting 'export API_KEY=value' where value can be any string of your choice.
