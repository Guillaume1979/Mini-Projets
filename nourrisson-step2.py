



import matplotlib.pyplot as plt
import csv

plt.figure(figsize=(20,20))
plt.suptitle("Données médicales du nourrisson")

#### Graphe Poids ####

#Nuage de point des données du nourrisson
x=[]
y=[]
with open ('./mesures.csv','r') as csvfile:
    donnees = csv.reader(csvfile,delimiter=';')
    
    entete = True
    
    for row in donnees :
        if entete:
            entete = False
            continue
        
        x.append (int(row[0]))
        y.append (float(row[1]))

#Courbes poids norme garçon
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]
x5=[]
y5=[]
with open ('./poids-age-garcon-0-60-light.csv','r') as csvfile:
    donnees = csv.reader(csvfile,delimiter=';')
    
    entete = True
    
    for row in donnees :
        if entete:
            entete = False
            continue
        x1.append (int(row[0]))
        y1.append (float(row[1]))        
        x2.append (int(row[0]))
        y2.append (float(row[2]))
        x3.append (int(row[0]))
        y3.append (float(row[3]))
        x4.append (int(row[0]))
        y4.append (float(row[4]))
        x5.append (int(row[0]))
        y5.append (float(row[5]))


plt.subplot (1,3,1)

plt.scatter(x,y,label="Données du nourrisson",color="green")# Affiche du nuage (on peut le mettre à la fin aussi avec les autres courbes)
plt.plot(x1,y1,label="5% poids")
plt.plot(x2,y2,label="25% poids")
plt.plot(x3,y3,label="50% poids")
plt.plot(x4,y4,label="75% poids")
plt.plot(x5,y5,label="95% poids")

plt.xlabel("Mois")
plt.ylabel("Poids en kg")
plt.title("Courbes de Poids du nourrisson")
plt.legend()
plt.grid()


#### Graphe taille ####

#Nuage de point des données du nourrisson
x=[]
y=[]
with open ('./mesures.csv','r') as csvfile:
    donnees = csv.reader(csvfile,delimiter=';')
    
    entete = True
    
    for row in donnees :
        if entete:
            entete = False
            continue
        
        x.append (int(row[0]))
        y.append (float(row[2]))



#Courbes taille norme garçon
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]
x5=[]
y5=[]
with open ('./taille-age-garcon-0-60-light.csv','r') as csvfile:
    donnees = csv.reader(csvfile,delimiter=';')
    
    entete = True
    
    for row in donnees :
        if entete:
            entete = False
            continue
        x1.append (int(row[0]))
        y1.append (float(row[1]))        
        x2.append (int(row[0]))
        y2.append (float(row[2]))
        x3.append (int(row[0]))
        y3.append (float(row[3]))
        x4.append (int(row[0]))
        y4.append (float(row[4]))
        x5.append (int(row[0]))
        y5.append (float(row[5]))


plt.subplot (1,3,2)

plt.scatter(x,y,label="Données du nourrisson",color="green")# Affiche du nuage (on peut le mettre à la fin aussi avec les autres courbes)
plt.plot(x1,y1,label="5% poids")
plt.plot(x2,y2,label="25% poids")
plt.plot(x3,y3,label="50% poids")
plt.plot(x4,y4,label="75% poids")
plt.plot(x5,y5,label="95% poids")

plt.xlabel("Mois")
plt.ylabel("Taille en cm")
plt.title("Courbes de taille du nourrisson")
plt.legend()
plt.grid()

#### Graphe périmètre cranien ####

#Nuage de point des données du nourrisson
x=[]
y=[]
with open ('./mesures.csv','r') as csvfile:
    donnees = csv.reader(csvfile,delimiter=';')
    
    entete = True
    
    for row in donnees :
        if entete:
            entete = False
            continue
        
        x.append (int(row[0]))
        y.append (float(row[3]))



#Courbes périmètre cranien norme garçon
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]
x5=[]
y5=[]
with open ('./perim-cra-age-garcon-0-60-light.csv','r') as csvfile:
    donnees = csv.reader(csvfile,delimiter=';')
    
    entete = True
    
    for row in donnees :
        if entete:
            entete = False
            continue
        x1.append (int(row[0]))
        y1.append (float(row[1]))        
        x2.append (int(row[0]))
        y2.append (float(row[2]))
        x3.append (int(row[0]))
        y3.append (float(row[3]))
        x4.append (int(row[0]))
        y4.append (float(row[4]))
        x5.append (int(row[0]))
        y5.append (float(row[5]))


plt.subplot (1,3,3)

plt.scatter(x,y,label="Données du nourrisson",color="green")# Affiche du nuage (on peut le mettre à la fin aussi avec les autres courbes)
plt.plot(x1,y1,label="5% poids")
plt.plot(x2,y2,label="25% poids")
plt.plot(x3,y3,label="50% poids")
plt.plot(x4,y4,label="75% poids")
plt.plot(x5,y5,label="95% poids")

plt.xlabel("Mois")
plt.ylabel("Taille en cm")
plt.title("Courbes du périmètre cranien du nourrisson")
plt.legend()
plt.grid()

plt.show()






