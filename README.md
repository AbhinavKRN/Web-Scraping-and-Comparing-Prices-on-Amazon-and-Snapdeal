Web Scraping and Comparing Prices on Amazon and Snapdeal
Overview
This Python script allows you to search for a product on Amazon and Snapdeal and retrieve their respective product listings along with their prices. It then presents the search results in a user-friendly format, making it easy to compare prices for the same product on both e-commerce platforms.

Dependencies
Python 3.x
requests library: Used for making HTTP requests to Amazon and Snapdeal's websites.
BeautifulSoup from bs4 library: Used for parsing the HTML content of the web pages.
time library: Used to introduce a delay between HTTP requests to avoid overloading the servers.
tabulate library: Used to format the search results into a neat and readable tabular format.
How to Use
Run the script.
Enter the name of the product you want to search for when prompted.
The script will then scrape the Amazon and Snapdeal websites for product listings and prices.
It will display the search results for both websites in a user-friendly format, allowing you to compare prices for the same product.
Supported Websites
Amazon.in: The script searches for the product on Amazon India.
Snapdeal.com: The script searches for the product on Snapdeal.
Code Description
The script defines two functions, search_amazon_product(product_name) and search_snapdeal_product(product_name), which perform the web scraping for Amazon and Snapdeal, respectively.
It sets user-agent headers to simulate a web browser when making HTTP requests.
It uses BeautifulSoup to parse the HTML content of the search results and extract product names and prices.
The main function main() takes user input for the product name, calls the search functions, and displays the results using the tabulate library for Snapdeal and a simple list for Amazon.
It displays the results with product names and their corresponding prices.
Note
Web scraping may be subject to the terms of service of the respective websites, so use this script responsibly and consider the legality and ethical implications of web scraping in your region.
