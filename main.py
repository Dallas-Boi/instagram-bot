# Made Friday, April 5th, 2024
# Makes a working instagram bot

from time import sleep
from selenium import webdriver

browser = webdriver.Opera()

browser.get('https://www.instagram.com/')

sleep(5)

browser.close()