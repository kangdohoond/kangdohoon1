import sys, requests
from bs4 import BeautifulSoup
from urllib import parse
from selenium import webdriver
from selenium.webdriver.ie.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import webbrowser as web