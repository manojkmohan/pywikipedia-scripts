#!/usr/bin/python
# -*- coding: utf-8 -*-

"""ഒരു സൂചികാതാളിലെ എല്ലാ പേജുകളിലുള്ള ഉള്ളടക്കവും ഒരു പുതിയ പേജിലേക്ക് എഴുതാൻ
നിർമ്മിച്ചത്: ബാലശങ്കർ (ബാലു)
നന്ദി: സുനിൽ വി.എസ്
05/01/2013
"""

import wikipedia
import pagegenerators
import codecs

siteFamily	= 'wikisource'
siteLangCode	= 'ml'
indexPage       = ur'Vancheeshageethi.djvu' #ഇൻഡെക്സ് താളിന്റെ പേര്. 
myNumber = 14
pageNamespaceId = 106
resultPage      = ur'user:Balasankarc/test' 

wikiSite = wikipedia.Site(code=siteLangCode, fam=siteFamily)
myResultPage=wikipedia.Page(site=wikiSite,title=resultPage)
#താളുകളിലെ ടെക്സ്റ്റ് എടുക്കുന്നു
for i in range(1,myNumber+1):
	myTitle='Page:'+indexPage+'/'+str(i)
	myPage=wikipedia.Page(site=wikiSite,title=myTitle)
	myText = myPage.get()
	myResultPage.append(myText)
	wikipedia.output(myPage.title())
	
wikipedia.stopme()


