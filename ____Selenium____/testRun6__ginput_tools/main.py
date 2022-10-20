from encodings import utf_8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import pandas as pd
import re


xls = pd.ExcelFile(r"New Sentences.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['Banglish'].astype('string')


website_1 = "https://www.google.com/inputtools/try/"

s = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(website_1)


select_lang = driver.find_element(
    By.XPATH, '//div[contains(@class,"goog-inline-block goog-menu-button-outer-box")]')
select_lang.click()
time.sleep(5)

in_text = driver.find_element(
    By.XPATH, '//div[@id="democontainer"]/textarea')


# unmodified = [
# "egula ektu besi somoy sapekko,, tai try korina.. amr eto dorjo nai… Kali Nethunter or AircrackNG diye hack kora jai, YouTube and google korle jante parven….",
# "last duita comment dhut trickbd te react option nai naile akai 100 ta kore ha ha ditam ar vai post datha parle eidao post koren ki bhabe mobile er screen on korte hoi onek helpfull hoto",
# "Youtube 'Video... Dile.. Valo Hoito…Jara Bujtece.Nah .Tara Video Dekhe Bujte Parto…!",
# ]

out_csv = []
output_file = "output_new_sentences.xlsx"

# for i in range(len(unmodified)):
for i in range(len(var1)):
# for i in range(10):
    modified = re.split('\s+|\…|\.+', var1[i])
    print(modified)
    for i in range(len(modified)):
        in_text.send_keys(f"{modified[i]} ")
        time.sleep(1)

    print("="*50)
    out_text = in_text.get_attribute("value")
    out_csv.append(out_text)
    time.sleep(.5)
    in_text.clear()


df3 = pd.DataFrame(out_csv, index=None)

with pd.ExcelWriter(output_file, mode='w') as writer:
    df3.to_excel(writer, sheet_name='Sheet1', header=None)

driver.quit()

# ! =======================================================================
# * driver.execute_script("arguments[0].innerText = 'Bangla'", select_lang)
# ! =======================================================================
