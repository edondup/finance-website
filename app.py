import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    # Display a table with portfolio of stocks

    # Query transactions db and get the sum of users holdings
    holdings = db.execute("SELECT symbol, SUM(shares) AS shares FROM trades WHERE userid = ? GROUP BY symbol", session["user_id"])

    # Variable to track the combined value of all stocks
    total_stock_value = 0

    # Loop through each owned stock lookup each symbol and get stock name, price and total value for each stock
    for holding in holdings:
        search = lookup(holding.get('symbol'))
        holding['name'] = search['name']
        holding['price'] = search['price']
        holding['total'] = holding['shares'] * holding['price']
        
        # Keep a running total value of all stocks combined
        total_stock_value = total_stock_value + holding['total']

    # Check how much cash user has in their account
    balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = balance[0]["cash"]

    return render_template("index.html", holdings = holdings, cash = cash, total_stock_value = total_stock_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    # Buy shares of stock
    # if buy form was posted update db and redirect to index
    if request.method == "POST":
        symbol, shares  = request.form.get("symbol"), request.form.get("shares")

        if shares and symbol:
            # check for valid whole number of shares
            if shares.isnumeric():
                shares = int(shares)
                if shares > 0:
                    stock = lookup(symbol.upper())
                    if stock:
                        price = (stock["price"])
                        print("price", price)
                        cost = price * shares

                        balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
                        # Check if user has enough money in their account to buy stock then update user and trade databases

                        # check the balance which is list returned by db exexute
                        # subtract the cost of the purchase from balance and create a buy entry into log db

                        new_balance = balance[0]["cash"] - cost
                        print("cost", cost)
                        print("new_balance", new_balance)
                        #check to make sure user has enough funds
                        if new_balance >= 0:
                            # Insert trade into trades database
                            db.execute("INSERT INTO trades (userid, type, shares, symbol, price) VALUES (?, ?, ?, ?, ?)", session["user_id"], "BUY", shares, stock["symbol"], price)
                            # Updated user cash holdings in the user db
                            db.execute("UPDATE users SET cash = ? WHERE id = ?", new_balance, session["user_id"])
                            return redirect("/")

                        else:
                            return apology ("Not enough funds to purchase stock")
                    else:
                        return apology ("Stock is not available. Please try another symbol")

            return apology("Please add a whole number of shares to purchase")
        else:
            return apology("Please provide stock symbol and number of shares")

    # show buy page if request method was get
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT symbol, type, shares, price, (shares * price) AS value, timestamp FROM trades WHERE userid = ?", session["user_id"])
    print(transactions)
    return render_template("history.html", transactions = transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # return quoted page with stock price if method was post
        symbol = request.form.get("symbol")
        if symbol is None:
            return apology("Please provide stock symbol")

        # use lookup function to get stock info by symbol
        else:
            stock = lookup(symbol.upper())
            # if the stock symbol doesn't exist return apology
            if stock is None:
                return apology("Invalid stock symbol")

        return render_template("quoted.html", stock = stock)

    # render page with form to get quote if method was get
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # require username, password and password confirmation
        username, password, confirmation = request.form.get("username"), request.form.get("password"), request.form.get("confirmation")

        if not username:
            return apology("Please add username")
        if not password or not confirmation:
            return apology("Please create a password")
        if password != confirmation:
            return apology ("Passwords do not match")

        # check if username already exists - db will return [] if username doesn't exist
        check = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if check == []:
            # hash password
            hash = generate_password_hash(password)

            user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            print(user)
            print(type(user))
            if user:
                session["user_id"] = user
                return redirect("/")
            else:
                return apology("Failure to register")
            # TODO add success message and redirect to login

        return apology("Invalid username and/or password")

    #if method is GET render register page
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        # create variables for stock symbol the number of shares to sell
        symbol, shares  = request.form.get("symbol"), request.form.get("shares")

        # Verify they have enough shares to sell
        # Query the db to get number of the user shares

        if symbol and shares:
            if shares.isnumeric():
                shares = int(shares)
                if shares > 0:
                    stock = db.execute("SELECT symbol, SUM(shares) AS shares, price FROM trades WHERE userid = ? AND symbol = ? ", session["user_id"], symbol)
                    print(stock)
                    print(type(stock))
                    if shares <= stock[0]["shares"]:
                        #store sell shares as a negative number note total will be negative on /history page because total = shares * price
                        shares = shares * -1

                        # lookup stock symbol to get current price
                        stockquote = lookup(symbol.upper())
                        price = stockquote['price']

                        # insert sale into the trades table
                        db.execute("INSERT INTO trades (userid, type, shares, symbol, price) VALUES(?, ?, ?, ?, ?)", session["user_id"], "SELL", shares, symbol, price)

                        # update user balance users table
                        cost = price * shares
                        balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
                        new_balance = balance[0]["cash"] - cost
                        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_balance, session["user_id"])


                        # if successful take user to the homepage
                        return redirect("/")

        # error: ask user for a stock symbol and number of shares
        return apology("Please enter a valid stock symbol and whole number of shares")



    # if method was get, render the page with with sell form to the user
    else:
        holdings = db.execute("SELECT symbol, SUM(shares) AS shares FROM trades WHERE userid = ? GROUP BY symbol", session["user_id"])

        return render_template("sell.html", holdings = holdings)