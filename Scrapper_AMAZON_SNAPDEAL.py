import requests
from bs4 import BeautifulSoup
import time
from tabulate import tabulate

def search_amazon_product(product_name):
    amazon_url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }
    time.sleep(2)
    response = requests.get(amazon_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    search_results = soup.find_all("div", {"data-component-type": "s-search-result"})
    amazon_products = []

    for result in search_results:
        product_name_element = result.find("span", {"class": "a-text-normal"})
        product_price_element = result.find("span", {"class": "a-price-whole"})

        if product_name_element and product_price_element:
            product_name = product_name_element.get_text().strip()
            product_price = product_price_element.get_text().strip()
            amazon_products.append((product_name, product_price))

    return amazon_products

def search_snapdeal_product(product_name):
    snapdeal_url = f"https://www.snapdeal.com/search?keyword={product_name.replace(' ', '+')}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"
    }
    time.sleep(2)
    response = requests.get(snapdeal_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    search_results = soup.find_all('div', class_='product-tuple-listing')
    snapdeal_products = []

    for result in search_results:
        product_name_element = result.find('p', class_='product-title')
        product_price_element = result.find('span', class_='lfloat product-price')

        if product_name_element and product_price_element:
            product_name = product_name_element.get_text().strip()
            product_price = product_price_element.get_text().strip()
            snapdeal_products.append((product_name, product_price))

    return snapdeal_products

def main():
    product_name = input("Enter the product name: ")

    snapdeal_products = search_snapdeal_product(product_name)
    amazon_products = search_amazon_product(product_name)

    snapdeal_table = []
    amazon_table = []

    for i, product in enumerate(snapdeal_products, start=1):
        snapdeal_table.append([i, product[0], f"₹{product[1]}"])

    print("\nSnapdeal Search Results:")
    print(tabulate(snapdeal_table, headers=["#", "Product Name", "Product Price"], tablefmt="pretty"))

    print("\nAmazon Search Results:")
    print("\n".join([f"{i}. {product[0]} - ₹{product[1]}" for i, product in enumerate(amazon_products, start=1)]))

if __name__ == "__main__":
    main()
