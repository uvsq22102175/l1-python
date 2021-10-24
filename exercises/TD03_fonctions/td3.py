# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    totalSeconde = temps[3] + temps[2] * 60 + temps[1] * 3600 + temps[0] * 3600 * 24
    return totalSeconde

temps = (3, 23, 1, 34)


print(type(temps))
print(tempsEnSeconde(temps))   


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    secondesReste = seconde % 60

    minutes = seconde // 60
    minutesReste = minutes % 60

    heures = minutes // 60
    heuresReste = heures % 24
    
    jours = heures // 24


    return (jours, heuresReste, minutesReste, secondesReste)

temps = secondeEnTemps(3600 * 24)


print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")


#fonction auxiliaire ici

def motsPlurielsJour(temps):
    """Renvoie un mot au pluriel / singulier ou pas de mot"""
    if temps[0] > 1 :
        jour = "jours"
    elif temps[0] == 1:
        jour = "jour"
    else:
        jour = ""
    return jour

def motsPlurielsHeure(temps):
    if temps[1] > 1:
        heure = "heures"
    elif temps[1]== 1:
        heure = "heure"
    else: 
        heure = ""
    return heure

def motsPlurielsMinutes(temps):
    if temps[2] > 1:
        minute = "minutes"
    elif temps [2] == 1:
        minute = "minute"
    else:
        minute = ""
    return minute

def motsPlurielsSeconde(temps):
    if temps[3] > 1:
        seconde = "secondes"
    elif temps[3] == 1:
        seconde = "seconde"
    else:
        seconde = ""
    return seconde

def afficheTemps(temps):
    """Renvoie une phrase donnant le temps passé en argument"""
    if temps[0] > 0:
        temps0 = temps[0]
    else:
        temps0 = ''
    
    if temps[1] > 0:
        temps1 = temps[1]
    else:
        temps1 = ''
    
    if temps[2] > 0:
        temps2 = temps[2]
    else:
        temps2 = ''
    
    if temps[3] > 0:
        temps3 = temps[3]
    else:
        temps3 = ''

    print(temps0, motsPlurielsJour(temps), temps1, motsPlurielsHeure(temps), temps2, motsPlurielsMinutes(temps), temps3, motsPlurielsSeconde(temps))


afficheTemps((1,0,14,23))


def demandeTemps():
    jour_ = int(input("Combien de jours ?"))
    while jour_ < 0 :
        jour_ = int(input("Cette valeur est incorrecte. Combien de jours ?"))
    
    heure_ = int(input("Combien d'heures ?"))
    while heure_ >= 24 or heure_ < 0:
        heure_ = int(input("Cette valeur est incorrecte. Combien d'heures ?"))
    
    minute_ = int(input("Combien de minutes ?"))
    while minute_ >= 60 or minute_ < 0:
        minute_ = int(input("Cette valeur est incorrecte. Combien de minutes ?"))
    
    seconde_ = int(input("Combien de secondes ?"))
    while seconde_ >= 60 or seconde_ < 0:
        seconde_ = int(input(" Cette valeur est inccorecte. Combien de secondes ?"))
    
    return (jour_,heure_,minute_,seconde_)

afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    sommeTempsSeconde = int(tempsEnSeconde(temps1)) + int(tempsEnSeconde(temps2))
    sommeTemps = secondeEnTemps(sommeTempsSeconde)
    return sommeTemps

afficheTemps(sommeTemps((2,3,4,25),(5,22,57,1)))