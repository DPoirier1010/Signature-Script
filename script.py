from jinja2 import Environment, FileSystemLoader
import os
import cherrypy
import io

#Author : DPoirier

# Set the path to the appropriate URL
logoAng1 = 'https://www.google.com/a/cpanel/nbifirm.com/images/logo.gif'
logoAng2 = ''
logoFr = 'https://s3.amazonaws.com/www.cabn.net/logo.gif'
logoBil = 'https://cabnimage.blob.core.windows.net/publiclogo/logocorpoBC.gif'
lang = 'https://s3.amazonaws.com/www.cabn.net/logo.gif'

#Variable for building the block of html
cssVar = '<span lang=\"FR-CA\" style=\"font-size:8pt;font-family:Verdana,sans-serif;color:rgb(0,50,78)\">'
cssVar2 = '</span>'
emailVar = '<span lang=\"FR-CA\" style=\"font-size:8pt;font-family:Verdana,sans-serif\"><a href=\"mailto:'
emailVar2 = '\"style=\"color:purple\">'
emailVar3 = '</a></span>'
#variable for the icon of tel cell fax...
logoTel = '<span style=\"font-size: 9pt; font-family: Wingdings; color: rgb(0, 50, 78);\">(</span>'
logoFax = '<span lang=\"FR-CA" style=\"font-size: 9pt; font-family: \'Wingdings 2\'; color: rgb(0, 50, 78);\">6</span>'
logoCell = '<span lang=\"FR-CA\" style=\"font-size: 9pt; font-family: Webdings; color: rgb(0, 50, 78);\">&Egrave;</span>'
logoTel2 = logoTel
logoCell2 = logoCell
#prompt for language
language = input('Choose between fr, eng or bil :')
nmbrAsst = input('How many person?     : ')

nmbrAsst = int(nmbrAsst)
flag = nmbrAsst

#path to the HTML for Jinja
templateModel = 'templateLoop.html'

#List to store the personne object
myList = []

#logic to give the good logo 
if language in ['fr', 'Fr', 'fR', 'FR']:
    lang = logoFr

elif language in ['ang', 'ANG', 'Ang', 'eng', 'ENG', 'Eng']:
    lang = logoAng1

elif language in ['bil', 'BIL', 'Bil']:
    lang = logoBil

#defining a personne class for all the rep that will go in myList[]
class personne:
    def __init__(self, nom, titre, titre2, tel, fax, cell, email):
        self.nom = nom
        self.titre = titre
        self.titre2 = titre2
        self.tel = tel
        self.fax = fax
        self.cell = cell
        self.email = email

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
#Getting information about every representant
for i in range(0, nmbrAsst):
    
    nom = input('name of the Person : ')
    titre = input('title of the person : ')
    titre2 = input('second title of the Person : ')
    tel = input('telephone number of the Person : ')
    fax = input('fax number of the Person : ')
    cell = input('cell number of the Person : ')
    email = input('email of the Person : ')
    nomConf = nom
    nom = '<b>' + cssVar + nom + cssVar2 + '</b>' + '<br>'
    titre = cssVar + titre + cssVar2 + '<br>'
    email = emailVar + email + emailVar2 + email + emailVar3 + '<br>' + '<br>'
    
    #building the string for the HTML block
    if titre2 == '':
        titre2 = ''  
    else:
        titre2 = cssVar + titre2 + cssVar2 + '<br>'

    if tel == '':
        tel = ''
    else:
        tel = '<br>' + logoTel + cssVar + tel + cssVar2 + '<br>'

    if fax == '':
        fax = ''
    else:
        fax = logoFax + cssVar + fax + cssVar2 + '<br>'

    if cell == '':
        cell = ''
    else:
        cell = logoCell + cssVar + cell + cssVar2 + '<br>'

    tempPerson = personne(nom, titre, titre2, tel, fax, cell, email)
    myList.insert(i,tempPerson)

    nmbrAsst = nmbrAsst - 1 
    

htmlMaster = ''
for y in myList:
    htmlBlock = ''
    htmlBlock = y.nom
    htmlBlock = htmlBlock + y.titre
    htmlBlock = htmlBlock + y.titre2
    htmlBlock = htmlBlock + y.tel
    htmlBlock = htmlBlock + y.fax
    htmlBlock = htmlBlock + y.cell
    htmlBlock = htmlBlock + y.email
    htmlMaster = htmlMaster +htmlBlock
#### Print the values and format for the block of html

#this is a tricky one, the address is variable, sometime 3, 4, 5 line
address = input('Copy paste the address : ')
address2 = input('second line of address : ')
address3 = input('third : ')
address4 = input('fourth : ')

#render to html
file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)
template = env.get_template(templateModel)
output = template.render(nom=nom, titre=titre, titre2=titre2, tel=tel,
                         fax=fax, cell=cell, email=email,address=address, lang=lang,
                         logoTel=logoTel, logoTel2=logoTel2, logoFax=logoFax, logoCell=logoCell,
                         logoCell2=logoCell2,nomConf=nomConf,flag=flag, htmlMaster = htmlMaster, address2=address2,address3=address3,address4=address4)
#write 
file = io.open('test.html', mode='w', encoding="utf-8")
file.write(output)
file.close()

