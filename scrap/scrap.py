import urllib2
import simplejson as son
import re
from BeautifulSoup import BeautifulSoup
link="http://www.wesleyan.edu/reslife/housing/residence/156_High.htm"
link2="http://www.wesleyan.edu/reslife/housing/residence/butterfield.htm"
link3="http://www.wesleyan.edu/reslife/housing/residence/west_college.htm"
link4="http://www.wesleyan.edu/reslife/housing/woodframe/162_church.htm"
link5="http://www.wesleyan.edu/reslife/housing/apartments/lo_rise.htm"
link6="http://www.wesleyan.edu/reslife/housing/woodframe/124%20High.htm"
link7="http://www.wesleyan.edu/reslife/housing/program/communityservice.htm"
link8="http://www.wesleyan.edu/reslife/housing/program/alpha.htm"
link9="http://www.wesleyan.edu/reslife/housing/woodframe/162_church.htm"
link10="http://www.wesleyan.edu/reslife/housing/woodframe/63_home.htm"
link11="http://www.wesleyan.edu/reslife/housing/woodframe/53_home.htm"
link12="http://www.wesleyan.edu/reslife/housing/program/psiu.htm"
link13="http://www.wesleyan.edu/reslife/housing/apartments/240_Court.htm"


testinglink=link13

json={}






response = urllib2.urlopen(testinglink)
linkflag=testinglink.split('/')
dirc = "http://www.wesleyan.edu/reslife/housing/"+linkflag[5]+"/"
page_source = response.read()
soup = BeautifulSoup(page_source)
name = soup.h1
img = soup.findAll('img')[1]
h3= soup.h3
plans = soup.findAll('li')
floorplans=[]
for plan in plans:
    floorplans.append(str(plan))
    

floorplan=[]   
x="href="

for plan in floorplans:
    if x in plan:
        floorplan.append(plan)

if floorplan==[]:
    planlinks ="False"

else:
    planlinks=[]
    for plan in floorplan:
        planlink=dirc + str(plan).split('"')[1]
        planlinks.append(planlink)
########################   
    

des2 = soup.find('div', {"id":"col2"})

des2 = re.sub(r'<br />',' ', str(des2))
#print des2
des2 = BeautifulSoup(des2)
des2 = ''.join(des2.findAll(text=True))
#print des2


####################
des = soup.find('div', {"id":"col2"})
des = str(des)#[52:][:-6]
#print des
######
img=str(img)
img=img.split('"')[-4]
if img[:3] == "../":
    img = "http://www.wesleyan.edu/reslife/housing/" + img[3:]
else:
    img = dirc + img
#print img
#######
name=str(name)[4:][:-5]
#print name
####

h3=str(h3)[4:][:-5]
h3=h3.split(",")

num_of_units=len(h3)
#print num_of_units
#print h3
h4=[]

for unit in h3:
    if "(quiet street)" in unit:
        quiet = 'Yes'
    else:
        quiet = 'No'
    h4.append(unit.strip())
#print h4
#print quiet

json["name"]=name
json["description"] = des2
json["img"] = img
json["num_of_units"]=num_of_units
json["floorplans"]=planlinks
json["quiet"]=quiet
#print json
json = (son.dumps(json))

