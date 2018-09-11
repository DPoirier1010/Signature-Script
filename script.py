from jinja2 import Environment, FileSystemLoader
import io


# Set the path to the appropriate URL
logoAng1 = 'https://cabnimage.blob.core.windows.net/publiclogo/logocorpoBC.gif'
logoAng2 = '523'
logoFr = 'https://s3.amazonaws.com/www.cabn.net/logo.gif'
logoBil = 'bil'
lang = 'https://s3.amazonaws.com/www.cabn.net/logo.gif'
# add a variable for path and name
# add variables for text that is common in all signatures

cssVar = '<span lang=\"FR-CA\" style=\"font-size:8pt;font-family:Verdana,sans-serif;color:rgb(0,50,78)\">'
cssVar2 = '</span>'


# add escape char
logoTel = '<span style=\"font-size: 9pt; font-family: Wingdings; color: rgb(0, 50, 78);\">(</span>'
logoFax = '<span lang=\"FR-CA" style=\"font-size: 9pt; font-family: \'Wingdings 2\'; color: rgb(0, 50, 78);\">6</span>'
logoCell = '<span lang=\"FR-CA\" style=\"font-size: 9pt; font-family: Webdings; color: rgb(0, 50, 78);\">&Egrave;</span>'
logoTel2 = logoTel
logoCell2 = logoCell

language = input('Choose between fr, eng or bil :')
nmbrAsst = input('How many person?     : ')
nmbrAsst = int(nmbrAsst)

#templateChoice = input('Assistant? y or n')

#if templateChoice in ['y', 'Y']:
#    templateModel = 'templateAssistant.html'

#else:
#   templateModel = 'template.html'

if language in ['fr', 'Fr', 'fR', 'FR']:
    lang = logoFr

elif language in ['ang', 'ANG', 'Ang']:
    lang = logoAng1

elif language in ['bil', 'BIL', 'Bil']:
    lang = logoBil

class personne:
    def __init__(self, nom, titre, titre2, tel, fax, cell, email):
        self.nom = nom
        self.titre = titre
        self.titre2 = titre2
        self.tel = tel
        self.fax = fax
        self.cell = cell
        self.email = email

while(nmbrAsst > 0):
    nmbrAsst = nmbrAsst - 1
    nom = input('name of the Person :')
    titre = input('title of the person : ')
    titre2 = input('second title of the Person :')
    tel = input('telephone number of the Person :')
    fax = input('fax number of the Person : ')
    cell = input('cell number of the Person : ')
    email = input('email of the Person : ')
    
    if tel == '':
        tel = ''
    else:
        tel = logoTel + cssVar + tel + cssVar2 + '<br>'

    if fax == '':
        fax = ''
    else:
        fax = logoFax + cssVar + fax + cssVar2 + '<br>'

    if cell == '':
        cell = ''
    else:
        cell = logoCell + cssVar + cell + cssVar2 + '<br>'

    personne(nom,titre, titre2, tel, fax, cell, email)
#### if else statement pour savoir si il faut print la ligne ou pas.. Un peu cabochon


#if telAdj == '':
#    telAdj = ''
#else:
#    telAdj = logoTel + cssVar + telAdj + cssVar2 + '<br>'
#
#if celAdj == '':
#    celAdj = ''
#else:
#    celAdj = logoCell + cssVar + celAdj + cssVar2 + '<br>'

#nom = input('name of the Person :')
#titre = input('title of the person : ')
# make this null if nothing is entered
#titre2 = input('second title of the Person :')
#tel = input('telephone number of the Person :')
# we might not need it, so if it's not used, don't output it
#fax = input('fax number of the Person : ')
#cell = input('cell number of the Person : ')
#email = input('email of the Person : ')
#nom2 = input('name of the second person  :')
#titreAdj = input('title of person 2 :')
#telAdj = input('telephone of the second person :')
#celAdj = input('cell of the second person :  ')
#emailAdj = input('email of the second person :')
#address = input('Copy paste the address')

#tel = logoTel + cssVar + tel + cssVar2 + '<br>'
#fax = logoFax + cssVar + fax + cssVar2 + '<br>'
#cell = logoCell + cssVar + cell + cssVar2 + '<br>'

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)
template = env.get_template(templateModel)
output = template.render(nom=nom, titre=titre, titre2=titre2, tel=tel,
                         fax=fax, cell=cell, email=email, nom2=nom2,
                         titreAdj=titreAdj, telAdj=telAdj, celAdj=celAdj,
                         emailAdj=emailAdj, address=address, lang=lang,
                         logoTel=logoTel, logoTel2=logoTel2, logoFax=logoFax, logoCell=logoCell,
                         logoCell2=logoCell2)


file = io.open('test.html', mode='w', encoding="utf-8")

file.write(output)

file.close()


# il faudrait aussi ajouter une option pour le nombre d'assistant ++
# Rajouter des valeurs pour differentes ligne pour l'addresses +++
# Peut etre faire un array +++
# si il y a des accents les changer pour leur symbole en html ++++
