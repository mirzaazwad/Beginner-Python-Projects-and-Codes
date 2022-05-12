In this task, we will sequentially build a simple web scraper. All of
the codes will use Python 3.9 or below and use only the standard
library.
You will write a python script that,


Step 00: Read the url and output folder name from the user using
`input`


Step 01: Given an url, verify if the url is a valid url or not.
Consider a url valid if it has the `http://` or `https://` or `ftp://`
scheme and contains a subdomain (eg. google, facebook) and domain (eg.
com, net). Print a descriptive error (what problems are in the url)
and stop the execution of the program with exit code -1 if the url is
invalid.


Step 02: Use the given url, to download the html source for the
website. (bonus: Save it to a file)


Step 03: Using regular expressions, find every image tag (<img>) in
the website and download the image files into the folder


Step 04: Use command line arguments instead of `input` to get the url
and output location (bonus: Use argument parsing and default
parameters)
