from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome(executable_path = r"D:\codding\code files\WebScrapping\chromedriver.exe")
browser.get(START_URL) 
time.sleep(10)

def scrape(): 
    headers = [["V_Mag.", "Proper_Name", "Bayer_designation", "Distance(ly)", "Spectral_Class","Mass","Radius","Luminosity"]]
    planet_data = [] 
    for i in range(0, 4): 
        soup = BeautifulSoup(browser.page_source, "html.parser") 
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}): 
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
            planet_data.append(temp_list) 
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click() 
    with open("project-127.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(planet_data) 
scrape
