# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[3] + temps[2] * 60 + temps[1] * 3600 + temps[0] * 3600 * 24


temps = (3, 23, 1, 34)


print(type(temps))
print(tempsEnSeconde(temps))   


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    secondesReste = seconde % 60
    minutes = seconde // 60
    minutesReste = seconde % 60
    heures = minutes // 60
    heuresReste = minutes % 24
    jours = heures // 24
    return (jours, heuresReste, minutesReste, secondesReste)


temps = secondeEnTemps(100000)


print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")