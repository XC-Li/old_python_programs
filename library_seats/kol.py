# Keep OnLine(wifi)
# Designed by Xc.Li
# Dec.2015
import urllib
import os
import re
import time
import winsound
def get_wifi():
    #get the current name of wifi
    #netsh wlan show interfaces
    flag = 0 #whether connected to a wifi?
    report = os.popen('netsh wlan show interfaces')
    for line in report:
        if re.search('^ *SSID',line):
            current_wifi_name = re.findall('^.*: (.*)',line)[0]
            flag = 1
    if flag == 0:
        current_wifi_name = 0
    return current_wifi_name
def connect_wifi(wifi_name):
    # netsh wlan add profile filename="E:\WLAN-call me daddy.xml"
    # netsh wlan connect name="call me daddy" ssid="call me daddy" interface="WLAN"
    if wifi_name == 0:
        new_connection = '23-608'
    if wifi_name == '23-608':
        new_connection = '23-608'
        os.system('netsh wlan disconnect')
        time.sleep(2)
    # if wifi_name == 'call me daddy':
        # new_connection = '23-608'
    os.system('netsh wlan add profile filename="D:\OneDrive\Python\material\WLAN-'+new_connection+'.xml"')
    os.system('netsh wlan connect name="'+new_connection+'" ssid="'+new_connection+'" interface="WLAN"')
def func():
    while (True):    
        try:
            print 'Trying to connect Baidu...'
            urllib.urlopen('http://www.baidu.com')
            print 'Connection is OK!'
            break
        except:
            print 'Fail to connect Baidu!'
            print 'currently connected to:',get_wifi()
            connect_wifi(get_wifi())
            winsound.Beep(880,1000)
            print 'wait...'
            time.sleep(5) #it takes some time to establish a connection