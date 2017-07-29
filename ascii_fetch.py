from bs4 import BeautifulSoup
import requests
import glob
url_ascii='http://www.glassgiant.com/ascii/ascii.php'
data_ascii=[]
title='default_title'
art='default_art'
spam_number=0

for filename in glob.glob('*.jpg'):
	
	data = { 'ggfile':open(filename,'rb'),  }
	r = requests.post(url_ascii,files=data)
	soup = BeautifulSoup(r.content,'html.parser').find('body')
	data_ascii.append(soup.get_text())
	print('data fetched from glassgiant.com')
	'''print(soup.get_text())'''
	spam_number=spam_number+1
	title='HARARA Spam # '+str(spam_number)
	data={'title':title, 'art':soup.get_text()}
	r =requests.post('http://asciibabes.appspot.com/',data)
	print ("Ishan sites status: ",r.status_code, r.reason,'\n\n')


input("Press Enter to continue...")
while True:
	for text in data_ascii:
		spam_number=spam_number+1
		title='HARARA Spam # '+str(spam_number)
		data={'title':title, 'art':text}
		r =requests.post('http://asciibabes.appspot.com/',data)
		print ("Ishan sites status: ",r.status_code, r.reason,'\n\n')