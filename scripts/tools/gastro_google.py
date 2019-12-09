#!/usr/bin/env python

from selenium import webdriver
import time
import datetime

import subprocess as sp
from subprocess import PIPE

GASTURL='https://app.gastromatic.de/'
SCHEDULEURL=GASTURL+'app/#/workSchedule'
MAIL = 'zolboo.deb@gmail.com'
NAMESEPSTR='_'
TODAY=datetime.date.today()

# 1. open app
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
#  driver = webdriver.Chrome(options=options)
driver = webdriver.Firefox()
driver.get(SCHEDULEURL)

# getting pass
p = sp.Popen(['pass', 'gastromatic.de/'+MAIL], stdin=PIPE, stdout=PIPE, stderr=PIPE,
            universal_newlines=True)
gaPass = p.communicate()[0][:-1]

username = driver.find_element_by_id("exampleInputEmail1")
password = driver.find_element_by_id("exampleInputPassword1")

# 2. login
username.send_keys(MAIL)
password.send_keys(gaPass)

driver.find_element_by_id('send-signin').click()

driver.implicitly_wait(10) # seconds
time.sleep(10)
driver.get(SCHEDULEURL)
print('Waiting 10 more seconds')
driver.implicitly_wait(10) # seconds
time.sleep(10)
print('Lets begin')

# 3. wait till loaded
# 4. check if it is right week
# create day dict
def gadateToGcaldate(date):
    dateRaw = date.split('\n')[0]
    dayName, calDay = dateRaw.split(' ')
    tmp = calDay.split('.')
    nCalDay = str(TODAY.year)+'/'+tmp[1]+'/'+tmp[0]
    return nCalDay

def notify(title, text):
    p = sp.Popen(['notify-send',title, text], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    gcalRet = p.communicate()[0][:-1]

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#  4. find my arbeit

try:
    for week in range(0, 2, 1):
        for loc in driver.find_elements_by_xpath('//ul[@class="workspace-checkboxes"]'):
            loc.click()
            if not hasNumbers(loc.text):
                continue

            days = [day.text for day in driver.find_elements_by_xpath('//div[contains(@class,"day padding-8") and  @ng-repeat="day in weekDays"]')]
            calDays = [gadateToGcaldate(day) for day in days]
            print(calDays)
            for schichtRow in driver.find_elements_by_xpath('//div[@class="card-row"]'):
                for day, group in enumerate(schichtRow.find_elements_by_xpath('div[@class="card-cell card-cell-employee"]')):
                    if day==0:
                        continue
                    for schicht in group.find_elements_by_xpath('./div[@class="card no-select card-employee-view card-success"]'):
                        # check name
                    #  -   div 'card-header card-header-employee' contains 'Zolboo Erdenebayar'
                        #  print(str(day) + ' : ' +schicht.text)
                        start = schicht.find_element_by_xpath('.//span[@class="margin-right-5"]')
                        end = schicht.find_element_by_xpath('.//span[@class="margin-left-5"]')

                        genname = calDays[day-1].replace('/',NAMESEPSTR)+NAMESEPSTR+start.text.replace(':',NAMESEPSTR)+NAMESEPSTR+end.text.replace(':',NAMESEPSTR)
                        p = sp.Popen(['gcalcli', 'search', genname], stdin=PIPE, stdout=PIPE, stderr=PIPE,
                                    universal_newlines=True)
                        gcalRet = p.communicate()[0]
                        if genname in gcalRet:
                            print(genname + ' exists')
                            continue

                        print( 'Adding day:'+genname)
                        notify('adding', genname)

                        p = sp.Popen(['gcalcli', '--calendar', 'Job', 'quick',calDays[day-1]+' '+start.text+'-'+end.text+" "+genname], stdin=PIPE, stdout=PIPE, stderr=PIPE,
                                    universal_newlines=True)
                        gcalRet = p.communicate()[0][:-1]
                        print(str(gcalRet))
            driver.find_element_by_xpath('//a[@role="button" and @ng-click="nextWeek()"]').click()
            print('NextWeek: Waiting 10 more seconds')
            time.sleep(10)
except:
    notify('gastro', 'error')


driver.close()
