#!/usr/bin/env python

# Author: Benjamin Perez
# e-mail: josebenjaminp@gmail.com
#
# Este script lee todos los MP3 que estan dentro del archivo listaMP3.txt, para
# cargar este archivo solo tienes que hacer algo como esto:
#
# $ ls *.mp3 >> listaMP3.txt
#
# el comando anterior te los aniade todos los .mp3 al archivo listaMP3.txt
#
# Requerimientos:
# # aptitude install ipython python-eyed3
#
# Continuamos, para ejecutarlo tienes que hacer lo siguiente:
#
# $ ipython getLyrics.py
#
# la linea anterior te introduce al interprete, y de ahi llamamos a la funcion.
#
# In [1]: getLyrics(True)
#
# ojo en la ultima linea si es True escribe el .tex sino te lo escribe
# uno por uno los MP3
#
# El archivo listaMP3.txt tiene que estar en le mismo directorio donde
# lo ejecutas.
#
# Disfrutalo.
#
# Happy hacking ;-)

import eyeD3, locale, sys

pathFile = []

# en fileText se carga el archivo y luego se carga cada linea(cada nombre del .mp3)
# a la lista pathFile, esta lista es la que se usa para ir cargando los MP3
fileText = open("listaMP3.txt", "r")
for linea in fileText:
    pathFile.append(linea)

fileText.close()

# allLyrics - este se usa para cuando se quiere exportar a un .tex (LaTeX)
allLyrics = []
allLyrics.append("\documentclass[a4paper, 12pt]{article}\n")
allLyrics.append("\usepackage[spanish]{babel}\n")
allLyrics.append("\usepackage[utf8x]{inputenc}\n")
allLyrics.append("\usepackage{anysize}\n")
allLyrics.append("\marginsize{2cm}{2cm}{2cm}{2cm}\n")
allLyrics.append("\\title{My Lyrics}\n")
allLyrics.append("\\begin{document}\n")
allLyrics.append("\maketitle\n")
allLyrics.append("\\newpage\n")
#allLyrics.append("\\tableofcontents\n")
allLyrics.append("\\newpage\n")
allLyrics.append("\\begin{center}\n")
allLyrics.append("\large{\n")

# Para usar el encoding local
ENCODING = locale.getpreferredencoding()

# Esta fucnion abre todos los MP3 y saca sus tags y titles
# y empieza a escribir los archivos con las letras de los MP3
def getLyrics(opt=False):
    for mp3 in pathFile:
        mp3 = cleanMp3(mp3)
        trackInfo = eyeD3.Mp3AudioFile(mp3)
        tag = trackInfo.getTag()

        lTitle  = tag.getTitle().replace('\r','\n')
        title   = lTitle.encode(ENCODING,"remplace")

        if opt:
            loadAllLyrics(tag, title)
        else:
            writeOneForOne(tag, title)
    if opt:
        writeDocLyrics()

# Esta funcion solo borra los '\n' de cada linea que se leyo del archivo
# TO DO - hay que mejorar :-/
def cleanMp3(mp3):
    tam = len(mp3) - 1
    i = 0
    aux=''
    while i < tam:
        aux += mp3[i]
        i += 1
    return aux

# Este funcion escribe uno por uno cada tema.
def writeOneForOne(tag, title):
    lyrics = tag.getLyrics()

    cancion = ""
    for l in lyrics:
        lLang = l.lang
        if lLang == None:
            lLang = ""
        lDesc = l.description
        if lDesc == None:
            lDesc = ""
        lText = l.lyrics.replace('\r', '\n')
        cancion = lText.encode(ENCODING,"replace")

    outp = open(title, "w")
    outp.write(title+'\n')
    for linea in cancion:
        outp.write(linea)
    outp.write("\n")
    outp.close()

# Esta funcion escribe todos en un solo archivo, para luego pasarlo
# a un documento LaTeX
def loadAllLyrics(tag, title):
    lyrics = tag.getLyrics()

    cancion = ""
    for l in lyrics:
        lLang = l.lang
        if lLang == None:
            lLang = ""
        lDesc = l.description
        if lDesc == None:
            lDesc = ""
        lText = l.lyrics.replace('\r', '\n')
        cancion = lText.encode(ENCODING,"replace")

    allLyrics.append("\section{"+title+"}")
    allLyrics.append("\n")
    i = 0
    for linea in cancion:
        if linea == '\n' and i < 1:
            allLyrics.append("\\"+"\\")
            allLyrics.append("\n")
            i += 1
        else:
            if linea == '\n':
                allLyrics.append("\\vspace{1cm}\n")
            else:
                allLyrics.append(linea)
                i = 0
            i = 0

    allLyrics.append("\\newpage")
    #allLyrics.append("\n")

# Escribe el documento final, un .tex :-)
def writeDocLyrics():

    allLyrics.append("}")
    allLyrics.append("\end{center}\n")
    allLyrics.append("\end{document}")
    outp = open("documento.tex", "w")
    for linea in allLyrics:
        outp.write(linea)
    outp.write("\n")
    outp.close()

# Happy hacking ;-)

