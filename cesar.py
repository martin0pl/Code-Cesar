def chiffrement(texte, decalage):

    messageChiffre = ""

    decalage = decalage%26

    for c in texte:

        # traitement des caractères non lettre
        newOrdC = ord(c)

        # traitement des minuscules
        if ord(c)>=97 and ord(c)<=122:
            newOrdC = newOrdC+decalage
            if newOrdC>122:
                newOrdC = newOrdC%122 + 97-1

        # traitement des majuscules
        if ord(c)>=65 and ord(c)<=90:
            newOrdC = newOrdC+decalage
            if newOrdC>90:
                newOrdC = newOrdC%90 + 65-1

        messageChiffre += chr(newOrdC)

    return(messageChiffre)

def dechiffrementConnu(texte, decalage):

    messageDechiffre = ""

    decalage = decalage%26

    for c in texte:

        # traitement des caractères non lettre
        newOrdC = ord(c)

        # traitement des minuscules
        if ord(c)>=97 and ord(c)<=122:
            newOrdC = ord(c)-decalage
            if newOrdC<97:
                newOrdC = 122+1 - (97-newOrdC)

        # traitement des majuscules
        if ord(c)>=65 and ord(c)<=90:
            newOrdC = ord(c)-decalage
            if newOrdC<65:
                newOrdC = 90+1 - (65-newOrdC)

        messageDechiffre += chr(newOrdC)

    return(messageDechiffre)

def dechiffrementBruteForce(message):

    messagesPossibles = []

    # test de tous les décalages possibles
    for i in range(1,26+1):
        messagesPossibles.append(dechiffrementConnu(message,i))

    return(messagesPossibles)