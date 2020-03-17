#!/usr/bin/python3
# simple sequence slicing example
# Split up a URL in one of the following forms:
# - https://www.something.com
# - https://something.com
# - http://www.something.com
# - http://something.com
# "something" will print

url = input('Please enter a URL: ')

if "https" in url:
    if "www" in url:
        domain = url[12:-4]
    else:
        domain = url[8:-4]
elif "www" in url:
    domain = url[11:-4]
else:
    domain = url[7:-4]

print("Domain name: " + domain)
