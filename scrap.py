import requests
import time
from playsound import playsound

import bs4

import lxml


# total=extract.select(".cscore_score ")
# for i in total:
# 	k=i.text
# 	print(k)
prev=''


#print(total)
while 1:
	extract=requests.get('https://www.espncricinfo.com/series/8674/game/1202251/west-indies-women-vs-india-women-3rd-odi-icc-womens-championship-2017-18-2021')
	#print(type(extract))
	extract=bs4.BeautifulSoup(extract.text,"lxml")
	total=extract.select(".cscore_score")
	k=total[1].text.split()
	#k=total[1].text

	print(k[1])
	if k[1]==prev:
		continue
	
	
	else:
		prev=k[1]

		for i in extract.select('.over-score'):
			x=i.text
			#print(x)
			break
		#print(x)
		
		if x=="4":
			playsound('/home/harshit/Documents/script_pro/four.mp3')
			continue
		if x=='6':
			playsound('/home/harshit/Documents/script_pro/SIX.mp3')
			continue
		if x=='W':
			playsound('/home/harshit/Documents/script_pro/wicket.mp3')
			continue
		time.c(10)
	







