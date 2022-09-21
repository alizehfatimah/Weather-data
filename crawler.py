from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import wget
import csv
import pandas as pd

DRIVER_PATH = "C:/Users/Alizeh Fatima/OneDrive/Desktop/Ahsan crolla/chromedriver_win32/chromedriver.exe"
download_dir = '../Ahsan crolla'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.maximize_window()
action = ActionChains(driver)
data_dict = {'time': 0, 'temperature': 999}
timelist = []
temperature = []

#for i in range(1,13):
link = 'https://www.timeanddate.com/weather/usa/chicago/historic?month='+str(12)+'&year=2021'
driver.get(link)
dropdown_element = driver.find_element_by_xpath("//select[@id='wt-his-select']")
opt = Select(dropdown_element)
for op in opt.options:
    print('option '+ op.get_attribute('innerHTML'))
    opt.select_by_visible_text(op.get_attribute('innerHTML'))
    time.sleep(0.8)
    rows = len(driver.find_elements_by_xpath("//table[@id='wt-his']/tbody/tr"))
    for i in range(1,rows+1):
        time_element = driver.find_element_by_xpath("//table[@id='wt-his']/tbody/tr["+str(i)+"]/th").get_attribute('innerHTML')
        if '53' in time_element:
            temp_element = (int(driver.find_element_by_xpath("//table[@id='wt-his']/tbody/tr["+str(i)+"]/td[2]").get_attribute('innerHTML').split('&')[0]) - 32) * 5/9
            print(temp_element)
            for i in range(0,60):
                timelist.append(time_element)
                temperature.append(temp_element)
action.perform()

d = pd.DataFrame(data=list(zip(timelist,temperature)),columns=['timestamp', 'temperature'])
d.to_csv('december_data.csv')
print(len(d))

#driver.get('https://www.timeanddate.com/weather/usa/chicago/historic?month=1&year=2021')


# ads = driver.find_elements_by_tag_name("iframe")

# if len(ads) > 0:
#     print("Ad Found\n")
#     driver.execute_script("""
#         var elems = document.getElementsByTagName("iframe"); 
#         for(var i = 0, max = elems.length; i < max; i++)
#              {
#                  elems[i].hidden=true;
#              }
#                           """)
#     print('Total Ads: ' + str(len(ads)))
# else:
#     print('No frames found')


