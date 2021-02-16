# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string


def nombre(n):

        print("les nombres premiers inférieurs à {} :\n2".format(n), end=', ')
        for i in range(3, n, 2):
            boo = False
            for j in range(3, i, 2):
                if i % j == 0:
                    boo = True
                    break
            if boo == False:
                print(i, end=', ')




def cesar(n, texte):
    texte = texte.lower().replace(' ', '')
    alphabet = list(string.ascii_lowercase)
    alphabetDecale = alphabet[n:] + alphabet[:n]
    texteCrypte = ''
    for i in range(len(texte)):
        texteCrypte += alphabetDecale[alphabet.index(texte[i])]
    return texteCrypte


def dechiffrerCesar(n, texteCrypte):
    texteCrypte = texteCrypte.lower().replace(' ', '')
    alphabet = list(string.ascii_lowercase)
    # definir un alphabet avec decalage de n lettres
    alphabetDecale = alphabet[n:] + alphabet[:n]
    texteNormal = ''
    for k in range(len(texteCrypte)):
        texteNormal += alphabet[alphabetDecale.index(texteCrypte[k])]
        
    return texteNormal


def hack(texteNormal, texteCrypte):
    keys = range(26)
    for key in keys:
        texteNormal = texteNormal.lower().replace(' ', '')
        alphabet = list(string.ascii_lowercase)
        alphabetDecale = alphabet[key:] + alphabet[:key]
        texteCrypte = ''
        for k in range(len(texteNormal)):
            texteCrypte += alphabetDecale[alphabet.index(texteNormal[k])]
        print("key={}".format(key), "------" + texteNormal + " ------- " + texteCrypte)

if __name__ == '__main__':
    print(cesar(1, "aziz"))
    print(dechiffrerCesar(1,"baja"))
    hack("aziz","baja")
