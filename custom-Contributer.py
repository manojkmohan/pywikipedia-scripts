#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ഒരു താളിലെയും അതിന്റെ ഉപതാളുകളിലെയും സംശോധകരുടെ പട്ടികയുണ്ടാക്കാൻ.
പ്രധാനമായും വിക്കിഗ്രന്ഥശാലക്കായി.
നിർമ്മിച്ചത്: സുനിൽ വി.എസ്. - സരയുവിനൊപ്പം
തിയതി: 2012-02-08
പതിപ്പ്: 1

കൂട്ടിച്ചേർക്കാനുള്ള കാര്യങ്ങൾ
==================
1. സ്റ്റാറ്റസോ എഡിറ്റ് സമ്മറിയോ നോക്കി പ്രൂഫ് വായിച്ചവരേയും സാധൂകരിച്ചവരേയും വേർതിരിക്കുക

"""

import wikipedia
import pagegenerators
import codecs

#പ്രധാന പ്രോഗ്രാം ഇവിടെ തുടങ്ങുന്നു. 
#ആവശ്യത്തിനനുസരിച്ച് മാറ്റങ്ങൾ ഇതിനു താഴെ വരുത്തുക
siteFamily	= 'wikisource'
siteLangCode	= 'ml'
workingPage	= ur'കിരണാവലി'           #ഏതു താളിൽ പണിചെയ്യണം?
indexPage       = ur'കിരണാവലി.djvu' #ഇൻഡെക്സ് താളിന്റെ പേര്. ഇതുപയോഗിച്ചുതന്നെ പേജ് മേഖലയും പ്രോഗ്രാം സ്വയം പരിശോധിക്കും.
pageNamespaceId = 106                 #വിക്കിഗ്രന്ഥശാലയിലെ താൾ മേഖലയുടെ വിലാസം - ഇതിൽ മാറ്റം വരുത്തേണ്ടതില്ല.
resultPage      = ur'user:vssun/test' #ഫലം എവിടെത്തരണം?

#ആവശ്യത്തിനനുസരിച്ച് മാറ്റങ്ങൾ ഇതിനു മുകളിൽ വരുത്തുക

wikiSite = wikipedia.Site(code=siteLangCode, fam=siteFamily)

#പ്രധാനതാളിലെ സംശോധകരെ പരിശോധിക്കുന്നു.
myPage = wikipedia.Page(site=wikiSite,title=workingPage)
wikipedia.output(myPage.title())
myUsers = myPage.contributingUsers()

#പ്രധാനതാളിന്റെ ഉപതാളുകളിലെ സംശോധകരെ പരിശോധിക്കുന്നു.
for myPage in pagegenerators.PrefixingPageGenerator(workingPage+"/"):
	myUsers = myUsers.union(myPage.contributingUsers())
	wikipedia.output(myPage.title())

#സൂചികാതാളിലെ സംശോധകരെ പരിശോധിക്കുന്നു.
myPage = wikipedia.Page(site=wikiSite,title="index:"+indexPage)
wikipedia.output(myPage.title())
myUsers = myUsers.union(myPage.contributingUsers())


#താളുകളിലെ സംശോധകരെ പരിശോധിക്കുന്നു.
for myPage in pagegenerators.PrefixingPageGenerator(indexPage+"/",namespace=pageNamespaceId):
	myUsers = myUsers.union(myPage.contributingUsers())
	wikipedia.output(myPage.title())

wikipedia.output(str(myUsers))

#ഫലം വിക്കിയിലേക്കെഴുതാൻ
myResultText=ur""
for myUser in myUsers:
	myResultText=myResultText+"*[[user:"+myUser+"]]\n"
	wikipedia.output(myUser)
myResultPage=wikipedia.Page(site=wikiSite,title=resultPage)
myResultPage.put(myResultText,comment=ur"സംശോധകരുടെ പട്ടിക")
wikipedia.stopme()


