import sys
import time
import json
import os
import csv
import datetime
from datetime import datetime as dtimes
from urllib.parse import urlparse
sys.path.append('browsermob-proxy-py-master')
sys.path.append('browsermob-proxy-2.1.4/bin')
from browsermobproxy import Server
import browsermobproxy
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
f_obj=open("input.csv")
default_week='6';
#server = Server("/home/karthik/selenium-freelace/browsermob-proxy-2.1.4/bin/browsermob-proxy")
#server.start()
#proxy = server.create_proxy()
proxy = browsermobproxy.Client('localhost:8080')
tchost="localhost"
tcport=proxy.port
#from selenium import webdriver
profile  = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1);
profile.set_preference("network.proxy.http", tchost);
profile.set_preference("network.proxy.http_port", tcport);
profile.set_preference("network.proxy.ssl", tchost);
profile.set_preference("network.proxy.ssl_port", tcport);
profile.set_preference("network.proxy.ftp", "localhost");
profile.set_preference("network.proxy.ftp_port", tcport);
profile.set_preference("network.proxy.share_proxy_settings", "true");
#profile.set_proxy(proxy.selenium_proxy())
#profile.update_preference()
driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX,
  browser_profile=profile)
#driver = webdriver.Firefox(firefox_profile=profile)
#harname="response.har"
reader = csv.DictReader(f_obj, delimiter=',')
for line in reader:
   cdate=line['Date']
   if not cdate:
       cdate=str(datetime.datetime.now().date())
   ddate = cdate
   weeks_to_add = line['week']
   if not weeks_to_add:
      weeks_to_add = default_week;
   weeks_to_add = int(weeks_to_add)
   cdateobj = dtimes.strptime(cdate,'%Y-%m-%d')
   departdateobj = cdateobj + datetime.timedelta(weeks=weeks_to_add)
   departdate= str(departdateobj)
   proxy.new_har("v2gcar23gi.execute-api.us-east-1.amazonaws.com",options={'captureHeaders': True, 'captureContent': True})
   url="https://www.linescape.com/schedules;origin_search="+line['Origin']+";destination_search="+line['Destination']+";start_date_gte="+cdate+";start_date_lte="+departdate+";origin_id=30190;origin_type=port;destination_id=53220;destination_type=port"
   driver.get(url)
   time.sleep(60)
   #WebDriverWait(driver, 20).until(driver.execute_script('return document.readyState;') == 'complete')
   harname = line['Origin']+"_"+line['Destination']+".har"
   myFile = open(harname,'w')
   data = proxy.har
   #creates a new file with origin and destination name
   for entry in data['log']['entries']:
        url = entry['request']['url']
        urlparts = urlparse(entry['request']['url'])
        size_bytes = entry['response']['bodySize']
        response = entry['response']
        size_kilobytes = float(entry['response']['bodySize'])/1024
        mimetype = 'unknown'
        if 'mimeType' in entry['response']['content']:
            mimetype = entry['response']['content']['mimeType']
            if (urlparts.hostname.find('v2gcar23gi.execute-api.us-east-1.amazonaws.com') >= 0 and mimetype== 'application/json'):
       	        har_data=json.dumps(entry['response']['content']['text'])
       	        myFile.write( har_data );
       	        print(line)   
   myFile.close()
#server.stop()
driver.quit()
