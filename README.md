# EDs Finance
A website where users can create an account to manage an fictional portfolio of stocks.

## Overview
EDs Finance web app built with Python using the Flask framework and a SQLite database. I used bootstrap design the style of my site and Jinja to help generate and format the tables presented on it. 

### Getting Started
If you haven't already logged in you will be redirected to the login page where can either login or signup. When users create an account they are given $10,000 fake cash as welcome bonus to purchase stocks! In order to research stock prices before trading you may use the quote page to search stocks get a quote. Once are ready to make a trade you can use the buy page to purchase new stocks or the sell page to sell stocks already own. The history page will give a record of all your transactions while the home gives a breakdown of your current holdings and cash.

### Notes
I created this project as part of the [Harvard CS50s Introduction to Computer Science](https://cs50.harvard.edu/x/2023/) course. My site originally used an API request to check current stock prices on [IEX](https://www.iexexchange.io/). In order for this to work you needed to create a trial account and add your token as a environment variable. In order to demonstrate how the site works without requiring you to create an IEX account I have temporarily commented out the original lookupup function located in helpers.py. The lookup function currently only returns made up prices for the stock symbols AAAA, BBBB, CCCC and DDDD.
