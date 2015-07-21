"""Funtions for scraping data from the given link"""

from bs4 import BeautifulSoup
from urllib import urlopen

def get_html_text(link):
    """
    Gets html text from the page source of link provided and resturns bs4 object
    """
    text = urlopen(link)
    soup = BeautifulSoup(text,"lxml")
    return soup

def get_restaurant_names(soup):
    """
    Gets restaurant names from soup
    """
    restaurants = []
    for restaurant in soup.find_all("a", class_="result-title" ):
        restaurants.append(restaurant.string[:20])
    return restaurants

def get_costs(soup):
    """
    Gets costs for two for the respective restaurants from soup
    """
    costs = []
    for cost in soup.find_all("div", class_="grey-text"):
        costs.append(int(cost.contents[1][4:].replace(',','')))
    return costs

def get_ratings(soup):
    """
    Gets repective ratings
    """   
    ratings = []
    for rating in soup.find_all("div", class_="rating-div"):
        ratings.append(rating.string.strip())
    return ratings
