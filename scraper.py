from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome(executable_path = r"D:\codding\CodeFiles\WebScrapping\chromedriver.exe")
browser.get(START_URL) 
time.sleep(10)
headers = [['star','constellation','Right acension','Declination','App mag','Distance(ly)','spectral type','brown dwarf','Mass(m)','Radius(r)','orbital period','semimajor axis','Discovery year']]
planet_data = []
new_planet_data = []

def scrape(): 
    for i in range(0, 420): 
        soup = BeautifulSoup(browser.page_source, "html.parser") 
        for ul_tag in soup.find_all("ul", attrs={"class", "brown dwarfs"}): 
            li_tags = ul_tag.find_all("li") 
            temp_list = [] 
            for index, li_tag in enumerate(li_tags): 
                if index == 0: 
                    temp_list.append(li_tag.find_all("a")[0].contents[0]) 
                else: 
                    try: 
                        temp_list.append(li_tag.contents[0]) 
                    except: 
                        temp_list.append("")
            hyperlink_li_tag = li_tags[0]
            temp_list.append("https://en.wikipedia.org/wiki/List_of_brown_dwarfs"+hyperlink_li_tag.find_all("a",href = True)[0]["href"])
            planet_data.append(temp_list) 
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()

def scrape_more_data(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content,"html.parser")
    for tr_tag in soup.finall_all("tr",attrs = {"class":"fact_row"}):
        td_tags = tr_tag.findall("td")
        temp_list = []
        for td_tag in td_tags:
            try:
                temp_list.append(td_tag.finad_all("div",attrs = {"class":"value"})[0].contents[0])
            except:
                temp_list.append("")
            new_planet_data.append(temp_list)

scrape()
for data in planet_data:
    scrape_more_data(data[0])

final_planet_data = []

for index,data in enumerate(planet_data):
    final_planet_data.append(data + final_planet_data[index])

    with open("project-128.csv", "w") as f:
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(planet_data) 
