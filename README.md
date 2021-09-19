# csgo500train-claimer

Hello there csgo500 player. My name is Nick and i created this bot in order to help you claim your free train bux from csgo500.com.



***DISCLAIMER***

USE THIS BOT AT YOUR OWN RISK. I AM NOT RESPONSIBLE IN CASE OF ANY BANS THAT MIGHT GET TO YOU BY THE CSGO500 TEAM.



***NOTES***

First of all you can run this python script in :

1. Your local PC (Will need to install some thing first)
2. On a windows operated VPS.(Will need to install some things first too)

In order for the script to run all the time your pc will have to be open at all times so it is recommended to us a VPS because it will be open 24/7.


***INSTALLATION***

1. Install the latest python. -- https://www.python.org/downloads/
2. Google Chrome.
3. Check if your python installation is completed correctly. To make sure check : https://www.youtube.com/watch?v=AdUZArA-kZw&t=0s
4. Open cmd and type the following " pip install selenium "
5. Download the chromedriver from : https://sites.google.com/a/chromium.org/chromedriver/downloads ( Must check the correct version from your chrome by typing in the url Chrome://version check the first to digits of version e.g (91,92,93) and download the correct chromedriver.
6. Extract the chromedriver.exe file you just downloaded to C:\Program Files(x86)\
7. Download my repository and extract it to your desktop : https://github.com/Nrentzilas/csgo500train-claimer/archive/refs/heads/main.zip
8. Now you are halfway there :P 


Now

1. Locate your Google chrome installation folder ( Usually it is cd C:\Program Files\Google\Chrome\Application\ )
If it is different than that you will have to change it accordingly
2. Find your profile setting path of google chrome. To do so type on your Google Chrome url -> chrome://version , it will be displayed as " Profile Path: " 
3. Go ahead and save the path of " Profile Path: " you will need it later

1. Open your cmd
2. Type cd C:\Program Files\Google\Chrome\Application\                                 \\ or your own chrome installation path
3. Type cmd --> chrome.exe --remote-debugging-port=9222 --user-data-dir="    "            \\ between  the " "  Paste the Profile Path you copied above. 
4. A Chrome window should have appeared.
5. Open another cmd                                                           \\ now you should locate the files you downloaded from my repository and find csgo500train.py     
6. Type cd "   "                                                               \\ Between the " " input the path of the csgo500train.py
7. Type python csgo500train.py

The script should be running just fine now

Enjoy your free bux :)
















