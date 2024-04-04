from bs4 import BeautifulSoup
import requests
# with open("links.html") as file:
#     content = file.read()
# soup = BeautifulSoup(content,"html.parser")
# print(soup.prettify())# scraps the whole page
# print(soup.title)# title of the page in htmml tag
# print(soup.title.string) #title of the page
# print(soup.a) #printing all the anchor tags
# anchor_tags = soup.find_all(name="a")
# print(anchor_tags)
# print("First anchor tag\n",anchor_tags[1])
# print("Displaying the text of all anchor tags")
# for _ in anchor_tags:
#     print(_.string)
#
# paragraph = soup.select(selector=".para")
# print(paragraph)
#
# for _ in paragraph:
#     print(_.string)
# url = "https://ntu.edu.pk/"
# response = requests.get(url=url)
# data = response.text
# soup = BeautifulSoup(data,"html.parser")
# print(soup.title)
# print(soup.title.string)
#
# anchor_tags = soup.find_all(name="a")
# for _ in anchor_tags:
#     print(_)
#
# anchor_tags = soup.find_all(name="a",class_="h6")
# for _ in anchor_tags:
#     print(_.text.strip())


# url = "https://www.empireonline.com/"
# response = requests.get(url=url)
# data= response.text
# soup = BeautifulSoup(data,"html.parser")
# # print(soup.prettify())
# print(soup.title)
# span_tag = soup.find_all(name="span")
#
# movies_title = [movie.get_text() for movie in span_tag]
# print(movies_title[::-1])


import os
from selenium import webdriver

os.environ['PATH'] += r"C:/SeleniumDriver"
driver = webdriver.Chrome()
# download-buttons-win
driver.get("https://code.visualstudio.com/")
driver.implicitly_wait(3)
my_element = driver.find_element("id","download-buttons-win")
my_element.click()
link_click = driver.find_element("id","direct-link")
link_click.click()
