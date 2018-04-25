from selenium import webdriver

test_site = 'http://hq.h.l9:8000'
browser = webdriver.Firefox()
browser.get(test_site)

assert 'User list' in browser.title
