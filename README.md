# Web-Scrapping
Web Scrapping using python libraries - Requests and BeautifulSoup

# Getting Started
Install our tools (preferably in a new virtualenv)::

    pip install bs4
    pip install requests
    pip install lxml

# Web scrapping algorithm
1. requests "the website url"
2. finds all the the text
3. cleans code from the text
4. appends text to an array
5. prints the array

# What is in Nseindia folder
Saving the live data of nse india option chains in csv files.
Calculating the strike price for five maximum OI, volume, change in OI for both Calls and Puts.
Showing all the calculated data in the form of tables using python GUI.

# How to run the code
run max_strike-price.py and nse_gui.py file

# What is in option_db folder
for a particular LTP value for both NIFTY and BANKNIFTY, it will give the reason for the rejection of strike price.

# how to run the code
run options_health.py and getLTP.py
