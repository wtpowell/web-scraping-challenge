#!/usr/bin/env python
# coding: utf-8




# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd





executable_path = {'executable_path': 'C:\chromedriver_win32\chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


mars_information = {}

def scrape_info():


    #input URL for mars news 
    url_mars = "https://redplanetscience.com/"
    browser.visit(url_mars)

    # HTML Object
    html_news = browser.html
    soup = bs(html_news, "html.parser")

    # Scrape the latest News Title and Paragraph Text
    news_title = soup.find("div", class_ = "content_title").text
    news_paragraph = soup.find("div", class_ = "article_teaser_body").text

    # Display scrapped news 
    print(news_title)
    print("-----------------------------------------")
    print(news_paragraph)


#JPL Mars Space Images - Featured Image

# Visit JPL Featured Space Image url through splinter module
    featured_image_url = 'https://spaceimages-mars.com/'
    browser.visit(featured_image_url)

    featured_image_html = browser.html
    img_soup = bs(featured_image_html, "html.parser")


# Find image url to the full size
    image_url = img_soup.find("img", {"class": "headerimage fade-in"})

# Display url of the full image
    featured_image_url = f"https://spaceimages-mars.com{image_url}"
    print("JPL Featured Space Image")
    print("-----------------------------------------")
    print(f"https://spaceimages-mars.com/{image_url['src']}")

#MARS FACTS WEBSCRAP

# Use Pandas to scrape the table on galaxyfacts-mars.com
    url_for_facts = "https://galaxyfacts-mars.com/"

    mars_facts = pd.read_html(url_for_facts)
    mars_facts

#Visit marshemispheres.com for images of mars
    url_hemisphere = "https://marshemispheres.com/"
    browser.visit(url_hemisphere)

    url_hemisphere = browser.html
    soup = bs(url_hemisphere, "html.parser")

# Scrape all items that contain mars hemispheres information
    hemispheres = soup.find_all("div", class_="item")

# Create empty list
    hemispheres_info = []

    hemispheres_url = "https://marshemispheres.com/"

# Loop through the list of all hemispheres information
    for i in hemispheres:
        title = i.find("h3").text
        hemispheres_img = i.find("a", class_="itemLink product-item")["href"]
        
        # Visit the link that contains the full image website 
        browser.visit(hemispheres_url + hemispheres_img)
        
        # HTML Object
        image_html = browser.html
        web_info = bs(image_html, "html.parser")
        
        # Create image url
        img_url = hemispheres_url + web_info.find("img", class_="wide-image")["src"]
        
        hemispheres_info.append({"title" : title, "img_url" : img_url})

    # print function for title and images
        print("")
        print(title)
        print(img_url)
        print("-----------------------------------------")


    browser.quit()
	
    return mars_information