# Amazon price scraper
This script will notify you when price of a certain product will be less than what you have mentioned.

## Library used
`smtplib`
`bs4`
`requests`

## How to use

- Change the User-Agent, according to your browser. [Refer here for more help.](https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/2)
- This script uses method `sendmail(fromaddr, toaddrs, msg)`, so Change your mail address for parameter `toaddrs` in the script.
- Change value for Product link you need the price to be checked for using variable `URL` and set a price for it, to be compared.
- Now you can set up a scheduler for this script, to check for price automatically.  It's easier to set up. [Each operating system comes with its own way of scheduling process.](https://automatetheboringstuff.com/schedulers.html) or just run the script manually as `python3 scraper.py`
