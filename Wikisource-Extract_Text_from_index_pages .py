#!/usr/bin/python
# -*- coding: utf-8 -*-

"""ഒരു സൂചികാതാളിലെ എല്ലാ പേജുകളിലുള്ള ഉള്ളടക്കവും ഒരു പുതിയ പേജിലേക്ക് എഴുതാൻ
നിർമ്മിച്ചത്: ബാലശങ്കർ സി
നന്ദി: സുനിൽ വി.എസ്
05/01/2013
"""

import wikipedia
import pagegenerators
import codecs

siteFamily	= 'wikisource'
siteLangCode	= 'ml'
indexPage       = ur'ശതമുഖരാമായണം.djvu' #സൂചിക താളിന്റെ പേര് രണ്ട് ' 'ന്റെ ഇടയിൽ കൊടുക്കുക. .djvu ചേർക്കാൻ മറക്കരുത്. 'സൂചിക' എന്ന് കൊടുക്കേണ്ട, അത് തന്നെ വന്നോളും.
myNumber = 27 #സൂചികാതാളുകളിലെ പേജുകളുടെ എണ്ണം കൊടുക്കുക. 
pageNamespaceId = 106 #ഗ്രന്ഥശാലയുടെ ഐഡി. മാറ്റേണ്ട ആവശ്യമില്ല. 
resultPage      = ur'User:Balasankarc\Test5' #ഫലം സൂക്ഷിക്കേണ്ട താളിന്റെ പേര് രണ്ട് ' 'ന്റെ ഇടയിൽ കൊടുക്കുക. ഉദാ: User:Balasankarc\Test5

wikiSite = wikipedia.Site(code=siteLangCode, fam=siteFamily)
myResultPage=wikipedia.Page(site=wikiSite,title=resultPage)

# ഇനിയാണ് മോനേ കളി... താളുകളിലെ ടെക്സ്റ്റ് എടുക്കുന്നു
for i in range(1,myNumber+1):
	myTitle='Page:'+indexPage+'/'+str(i)
	myPage=wikipedia.Page(site=wikiSite,title=myTitle)
	try:			#ഇനി പണ്ടാരമടങ്ങാൻ ഒരു ടൈപ്പ് ചെയ്യാത്ത പേജ് എങ്ങാനും വന്നുപെട്ടാലോ?
		myText = myPage.get()	#അങ്ങനെ ഉണ്ടെങ്കിൽ ലിവൻ എറർ കാണിക്കും. അതൊഴിവാക്കാനാണ് ആ try
		myResultPage.append(myText,comment=ur"ടെക്സ്റ്റ് വേർതിരിച്ചെടുക്കുന്നു")
		wikipedia.output(myPage.title())
	except:			#അങ്ങനെ ഉണ്ടെങ്കിൽ ഇങ്ങോട്ട് ചാടിക്കോളും
		continue	#ആ പേജ് മൈൻഡ് ചെയ്യണ്ട
	
wikipedia.stopme()


