from copy import copy
from PIL import Image, ImageDraw, ImageFont
img_orig = Image.open('Logo.png')
stats = ["ACS"]
stats1 = ["K", "D", "A", "ECON"]
im_width = img_orig.width
im_height = img_orig.height

names = {
    "as":"Valorant/Astra.jpg",
    "br":"Valorant/Breach.jpg",
    "ch":"Valorant/Chamber.jpg",
    "cy":"Valorant/Cypher.jpg",
    "je":"Valorant/Jett.jpg",
    "ki":"Valorant/Killjoy.jpg",
    "om":"Valorant/Omen.jpg",
    "ra":"Valorant/Raze.jpg",
    "sk":"Valorant/Skye.jpg",
    "so":"Valorant/Sova.jpg",
    "vi":"Valorant/Viper.jpg",
    "sa":"Valorant/Sage.jpg",
    "re":"Valorant/Reyna.jpg",
    "ka":"Valorant/Kayo.jpg",
    "bs":"Valorant/Brimstone.jpg",
    "ph":"Valorant/Pheonix.jpg",
    "ne":"Valorant/Neon.png",
    "yo":"Valorant/Yoru.png",
}



# pocet vals
font_size = 65
foont_size2 = 55
scoreboard = "Fonts/Scoreboard Regular.ttf"
mvp = "Fonts/acquire.otf"
height = 70

# trl c + ctrl v
def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T

# 1x mapa
mapa = ImageDraw.Draw(img_orig)
mapa.multiline_text((im_width/2, 200), input(), anchor="mm", fill=(0,0,0), font=ImageFont.truetype(font=mvp, size=120), align="center")
# 2x skore
print("")
score1 = ImageDraw.Draw(img_orig)
score1.multiline_text((75, 1200), input(),anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=350), align="right")
score2 = ImageDraw.Draw(img_orig)
score2.multiline_text((75, 1650), input(),anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=350), align="right")

#prvni obrazek, tabulka s obrazkem, jmenem a acs
def img1():
    img = copy(img_orig)
    n = len(stats) + 1 
    #objekt tabulky legendy
    tabulka = [ImageDraw.Draw(img) for _ in range(len(stats) + 1)]

    #pozice prvniho textu
    x = 185
    y = 1000

    width = 280
    
    #prvni tym
    Team1 = input(" ")
    vals = [[Team1, (138,14,23), 80], *stats]
    #jmeno tymu, legenda
    tabulka[0].multiline_text((x, y), vals[0][0] ,anchor="lm", fill=vals[0][1], font=ImageFont.truetype(font=scoreboard, size=vals[0][2]), align="left")
    x += width*3 + - 50
    tabulka[1].multiline_text((x, y), vals[1] ,anchor="lm", fill=(23,57,108), font=ImageFont.truetype(font=scoreboard, size=foont_size2), align="left")
    #hraci
    y += height
    players = [[input() for _ in range(5)] for i in range(n+1)]
    players = transpose(players)
    for i in range(5):
            x = 405
            temp = ImageDraw.Draw(img)
            temp.multiline_text((x, y), players[i][0] ,anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
            x += width + 150
            im = Image.open(names[players[i][1]])
            img.paste(im, (x, y-30))
            x += width - 150 
            temp = ImageDraw.Draw(img)
            temp.multiline_text((x, y), players[i][2] ,anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
            
            y += height

    #druhy tym

    x = 185
    y = 1450
    Team2 = input(" ")
    vals = [[Team2, (138,14,23), 80], *stats]
    #jmeno tymu, legenda
    tabulka[0].multiline_text((x, y), vals[0][0] ,anchor="lm", fill=vals[0][1], font=ImageFont.truetype(font=scoreboard, size=vals[0][2]), align="left")
    x += width*3 - 50
    tabulka[1].multiline_text((x, y), vals[1] ,anchor="lm", fill=(23,57,108), font=ImageFont.truetype(font=scoreboard, size=foont_size2), align="left")
    #hraci
    y += height
    players = [[input("") for _ in range(5)] for i in range(n+1)]
    players = transpose(players)
    for i in range(5):
            x = 405
            temp = ImageDraw.Draw(img)
            temp.multiline_text((x, y), players[i][0] ,anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
            x += width + 150
            im = Image.open(names[players[i][1]])
            img.paste(im, (x, y-30))
            x += width - 150
            temp = ImageDraw.Draw(img)
            temp.multiline_text((x, y), players[i][2] ,anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
            
            y += height
    
    img.show()
    img.save("v1/" + Team1 + "vs2"+Team2 + "_1.png")


def img2():
    img = copy(img_orig)
    n = len(stats1)
    tabulka = [ImageDraw.Draw(img) for _ in range(n+1)]

    #prvni tym
    x = 185
    y = 1000
    width = 100
    Team1 = input(" ")
    vals = [[Team1,(138,14,23), 80] , *stats1]
    for i, t in zip(tabulka, vals):
        if isinstance(t, list):    
            i.multiline_text((x, y), t[0], anchor="lm", fill=t[1], font=ImageFont.truetype(font=scoreboard, size=t[2]), align="left")
            x += width*6 - 50
        else:
            i.multiline_text((x, y), t ,anchor="lm", fill=(23,57,108), font=ImageFont.truetype(font=scoreboard, size=foont_size2), align="left")
            x += width
        

    players1 = [ [ input() for _ in range(5)] for _ in range(n+1) ]
    players1 = transpose(players1)

    y += height
    for i in players1:
        x = 405
        temp = ImageDraw.Draw(img)
        temp.multiline_text((x, y), i[0] ,anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
        x += width*6 - 270
        for t in i[1:]: 
            temp = ImageDraw.Draw(img)
            temp.multiline_text((x, y), t ,anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
            x += width
        y += height
    
    #druhy tym
    x = 185
    y = 1450
    width = 100
    Team2 = input(" ")
    vals = [[Team2, (138,14,23), 80] , *stats1]
    for i, t in zip(tabulka, vals):
        if isinstance(t, list):    
            i.multiline_text((x, y), t[0], anchor="lm", fill=t[1], font=ImageFont.truetype(font=scoreboard, size=t[2]), align="left")
            x += width*6 - 50
        else:
            i.multiline_text((x, y), t ,anchor="lm", fill=(23,57,108), font=ImageFont.truetype(font=scoreboard, size=foont_size2), align="left")
            x += width
        

    players1 = [ [ input() for _ in range(5)] for _ in range(n+1) ]
    players1 = transpose(players1)

    y += height
    for i in players1:
        x = 405
        temp = ImageDraw.Draw(img)
        temp.multiline_text((x, y), i[0], anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
        x += width*6 - 270
        for t in i[1:]: 
            temp = ImageDraw.Draw(img)
            temp.multiline_text((x, y), t, anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
            x += width
        y += height

    img.show()
    img.save("v1/"+Team1+"vs2"+Team2+"_2.png")

img1()
img2()