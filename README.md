# finance-website
A website where users can create an account to manage an imaginary portfolio of stocks.

## Overview
This website is a Python web app using the Flask framework that utlizes a SQLite database. I used bootstrap to style the webpage and Jinja to generate tables. When users create account they are given $10,000 to purchase stocks. Please do not create user names or passwords that you use anywhere else.

### Notes
I created this project as part of the [Harvard CS50s Introduction to Computer Science](https://cs50.harvard.edu/x/2023/) course. My site originally used an API request to check current stock prices on [IEX](https://www.iexexchange.io/). I created a free trial account on their website which has expired. Instead of creating another trial I account I replaced the lookup up function which can now only return made up prices for the stock symbols AAAA, BBBB, CCCC and DDDD.
