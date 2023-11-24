# EDs Finance
A website where users can create an account to manage a fictional portfolio of stocks of their choice. It can be a fun, risk-free way for users to practice and gain experience buying and selling assets that reflect real world prices.

## Overview
EDs Finance is a Python web app which uses the Flask framework. It uses a SQLite database to store data and Bootstrap to style the pages and provide alerts. Jinja is included on the templates to generate the tables of data for the user.

### The Website
If you haven't already logged in, you will be redirected to the login page where you can either login or signup. When users create an account, they are given $10,000 fake cash as a welcome bonus to purchase stocks. Lucky you! In order to research stock prices before trading, you may use the quote page to search stocks to get a price quote. Once you are ready to make a trade, you can use the buy page to purchase new stocks or the sell page to sell stocks you already own. The history page will give a record of all your transactions while the home gives a breakdown of your current holdings and cash.

### Getting Started
In order to run this program you need to download the repository. Navigate to the finance-website directory you downloaded. You may wish to create a virtual environment (if not skip to install dependencies with pip). See python [documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments) for more information and instructions on Windows. To create a virtual environment use `python3 -m venv .venv` followed by `.venv/bin/activate` to activate it. Install dependencies with `pip install -r requirements.txt`. Use the command `export FLASK_APP=app.py` in order to set the flask environment variable. In order to use real life stock prices you will need to follow the instructions at [CS50s project page](https://cs50.harvard.edu/x/2022/psets/9/finance/#configuring) and create an account at [IEX](https://www.iexexchange.io/). Then you will need to run `export API_KEY=value` where `value` is your passkey. Please see the [Notes](#notes) as I have changed my app to no longer require this trial account setup. Finally, run the command `flask run` to run a development server. To stop the server use `Command + .` (Mac) or  `CTRL + C`  (Windows). If you created a virtual environment enter `deactivate` to exit it.

### Notes
I created this project as part of the [Harvard CS50s Introduction to Computer Science](https://cs50.harvard.edu/x/2023/) course. My site originally used an API request to check current stock prices on [IEX](https://www.iexexchange.io/). In order for this to work you needed to create a trial account and add your token as an environment variable. In order to demonstrate how the site works without requiring you to create an IEX account I have temporarily commented out the original lookup function located in helpers.py. The lookup function now only returns made up static prices for the stock symbols AAAA, BBBB, CCCC and DDDD. You will still need to create an environment variable by executing `export API_KEY=value` where `value` can be any string of your choice like `abc` for example.
