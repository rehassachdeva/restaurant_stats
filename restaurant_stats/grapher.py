"""Function for plotting the graph"""

import matplotlib.pyplot as plt
from pylab import savefig, xlim
from numpy import arange

import scraper

def graph(link, outfile):
    """
    Plots the grraph and saves it in outfile
    """
    soup = scraper.get_html_text(link)
    restaurants = scraper.get_restaurant_names(soup)
    costs = scraper.get_costs(soup)
    ratings = scraper.get_ratings(soup)
                                    
    l = len(restaurants)
    
    plt.bar(range(l),costs,color="#CC0033")
    plt.ylabel("COSTS",fontsize=15,color="#330033")
    plt.xticks(arange(0.5,30.5,1.0), restaurants, ha="center", rotation=90)
    plt.xlabel("RESTAURANTS",fontsize=15,color="#330033")
    plt.xlim([0,l])

    for X, Y, Z in zip(range(l), costs, ratings):
        plt.annotate('{}'.format(Z), xy=(X,Y), xytext=(0,2),textcoords='offset points',fontsize=8,color="#330033")
        
    fig = plt.gcf()
    fig.subplots_adjust(bottom=0.4)
    fig.savefig(outfile)
