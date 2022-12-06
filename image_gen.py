from copy import copy
from PIL import Image, ImageDraw, ImageFont
from os.path import join
import sys

STATS = {
    "valorant_1": ["ACS"],
    "valorant_2": ["K", "D", "A", "ECON"],
    "empty": []
}

VALORANT_CHAR_ABBR = {
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
scoreboard = "./fonts/Scoreboard Regular.ttf"
mvp = "./fonts/acquire.otf"
height = 70

def transpose(matrix: list) -> list:
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T

def modify(stats: str, img: str, inp: str, o: str, d: str, quiet: bool) -> None:
    with open(inp, "r") as f:
        try:
            img = Image.open(img)
        except FileNotFoundError as err:
            print(f"{__file__}: {sys.stderr}: {err.strerror} \n Invalid file name")
            return
        im_width = img.width
        im_height = img.height
        n = len(STATS[stats])
        tabulka = [ImageDraw.Draw(img) for _ in range(n+1)]
        # 1x mapa
        mapa = ImageDraw.Draw(img)
        mapa.multiline_text((im_width/2, 200), f.readline().rstrip("\n"), anchor="mm", fill=(0,0,0), font=ImageFont.truetype(font=mvp, size=100), align="center")
        # 2x skore
        score1 = ImageDraw.Draw(img)
        score1.multiline_text((75, 1300), f.readline().rstrip("\n"),anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=350), align="right")
        score2 = ImageDraw.Draw(img)
        score2.multiline_text((75, 1750), f.readline().rstrip("\n"),anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=350), align="right")

        #prvni tym
        x = 300
        y = 1050
        width = 100
        Team1 = f.readline().rstrip("\n")
        vals = [[Team1,(138,14,23), 80] , *STATS[stats]]
        for i, t in zip(tabulka, vals):
            if isinstance(t, list):    
                i.multiline_text((x, y), t[0], anchor="lm", fill=t[1], font=ImageFont.truetype(font=scoreboard, size=t[2]), align="left")
                x += width*6 - 50
            else:
                i.multiline_text((x, y), t ,anchor="lm", fill=(23,57,108), font=ImageFont.truetype(font=scoreboard, size=foont_size2), align="left")
                x += width
            

        players1 = [ [ f.readline().rstrip("\n").rstrip("\n") for _ in range(5)] for _ in range(n+1) ]
        players1 = transpose(players1)

        y += height
        for i in players1:
            x = 330
            temp = ImageDraw.Draw(img)
            temp.multiline_text((x, y), i[0] ,anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
            x += width*6 - 270
            for t in i[1:]: 
                temp = ImageDraw.Draw(img)
                temp.multiline_text((x, y), t ,anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
                x += width
            y += height
        
        #druhy tym
        x = 300
        y = 1500
        width = 100
        Team2 = f.readline().rstrip("\n")
        vals = [[Team2, (138,14,23), 80] , *STATS[stats]]
        for i, t in zip(tabulka, vals):
            if isinstance(t, list):    
                i.multiline_text((x, y), t[0], anchor="lm", fill=t[1], font=ImageFont.truetype(font=scoreboard, size=t[2]), align="left")
                x += width*6 - 50
            else:
                i.multiline_text((x, y), t ,anchor="lm", fill=(23,57,108), font=ImageFont.truetype(font=scoreboard, size=foont_size2), align="left")
                x += width
            

        players1 = [ [ f.readline().rstrip("\n") for _ in range(5)] for _ in range(n+1) ]
        players1 = transpose(players1)

        y += height
        for i in players1:
            x = 330
            temp = ImageDraw.Draw(img)
            temp.multiline_text((x, y), i[0], anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
            x += width*6 - 270
            for t in i[1:]: 
                temp = ImageDraw.Draw(img)
                temp.multiline_text((x, y), t, anchor="lm", fill=(0,0,0), font=ImageFont.truetype(font=scoreboard, size=font_size), align="left")
                x += width
            y += height

        if not quiet:
            img.show()
        output = ""
        if d:
            output = join(output, d)
        if o:
            output = join(output, o)
        else:
            output = join(f"{Team1}_vs_{Team2}.png")
            print(output)
        if output[-4:] != ".png":
            output += ".png"
        try:
            img.save(output)
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{__file__}: {sys.stderr}: {err.strerror} \n Invalid directory")

