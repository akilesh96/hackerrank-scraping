
# coding: utf-8

# In[1]:


from selenium import webdriver
chrome_path = r"C:\Users\AKILESH\Desktop\Web scraping\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.hackerrank.com/contests/tna-klu/leaderboard/")


# In[6]:


posts = driver.find_elements_by_class_name("leaderboard-list-view")


# In[7]:


from openpyxl import Workbook
from openpyxl import load_workbook
wb = load_workbook('test.xlsx')
ws = wb["Sheet"]
for post in posts:
    temp = post.text.split("\n")
    name = ""
    driver_temp = webdriver.Chrome(chrome_path)
    driver_temp.get("https://www.hackerrank.com/"+temp[1])
    h3 = driver_temp.find_elements_by_tag_name("h3")
    if len(h3) != 0:
        name = h3[0].text
    driver_temp.close()
    ws.append([temp[0], name, temp[1], temp[2], temp[3]])
wb.save("test.xlsx")

