# TestScripter
A framework which allow you to write and run your script with master and slave machines.

Steps to execute
================

install request using "pip install request"

clone the below supported tool, extract them and place it besides the tracker.py file

https://github.com/lightbody/browsermob-proxy/releases/download/browsermob-proxy-2.1.4/browsermob-proxy-2.1.4-bin.zip
https://github.com/AutomatedTester/browsermob-proxy-py.git

run the selenium server

run the browsermob which is located in browsermob-proxy-2.1.4/lib using below command


 java -jar  browsermob-dist-2.1.4.jar 

Place ip in "localhost" location in py file.

run your scripts now
====================
python tracker.py 

it will write response besides the file with the name "response.har".

Place input.csv file besides the script.py file, will generate no of response files with the source and destination names.

Ex: "INNSA_DEHAM.har"
Update
