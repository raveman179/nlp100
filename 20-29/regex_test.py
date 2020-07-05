import re
lang_braces = re.compile(r'''(?:=.*?)?\[.*?(IMF\>.*?)\]$''')

string = '1兆5478億[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a=IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]'
print(lang_braces.sub(r'\1', string))