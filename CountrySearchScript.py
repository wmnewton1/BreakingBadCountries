from bs4 import BeautifulSoup
import requests
import re

reader = open("C:/Users/Guest 1/OneDrive/Documents/Breaking Bad/All_countries.txt")
lines = reader.read()
reader.close()
countryArr = lines.split("\n")

webpages = [["n"] * 16] * 5

# season 1
webpages[0][0] = "https://breakingbad.fandom.com/wiki/Pilot_subtitles"
webpages[0][1] = "https://subslikescript.com/series/Breaking_Bad-903747/season-1/episode-2-Cats_in_the_Bag"
webpages[0][2] = "https://subslikescript.com/series/Breaking_Bad-903747/season-1/episode-3-And_the_Bags_in_the_River"
webpages[0][3] = "https://subslikescript.com/series/Breaking_Bad-903747/season-1/episode-4-Cancer_Man"
webpages[0][4] = "https://subslikescript.com/series/Breaking_Bad-903747/season-1/episode-5-Gray_Matter"
webpages[0][5] = "https://subslikescript.com/series/Breaking_Bad-903747/season-1/episode-6-Crazy_Handful_of_Nothin"
webpages[0][6] = "https://subslikescript.com/series/Breaking_Bad-903747/season-1/episode-7-A_No-Rough-Stuff-Type_Deal"

# season 2
webpages[1][0] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-1-Seven_Thirty-Seven"
webpages[1][1] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-2-Grilled"
webpages[1][2] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-3-Bit_by_a_Dead_Bee"
webpages[1][3] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-4-Down"
webpages[1][4] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-5-Breakage"
webpages[1][5] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-6-Peekaboo"
webpages[1][6] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-7-Negro_Y_Azul"
webpages[1][7] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-8-Better_Call_Saul"
webpages[1][8] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-9-4_Days_Out"
webpages[1][9] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-10-Over"
webpages[1][10] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-11-Mandala"
webpages[1][11] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-12-Phoenix"
webpages[1][12] = "https://subslikescript.com/series/Breaking_Bad-903747/season-2/episode-13-ABQ"

# season 3
webpages[2][0] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-1-No_Ms"
webpages[2][1] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-2-Caballo_sin_Nombre"
webpages[2][2] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-3-IFT"
webpages[2][3] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-4-Green_Light"
webpages[2][4] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-5-Ms"
webpages[2][5] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-6-Sunset"
webpages[2][6] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-7-One_Minute"
webpages[2][7] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-8-I_See_You"
webpages[2][8] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-9-Kafkaesque"
webpages[2][9] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-10-Fly"
webpages[2][10] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-11-Abiquiu"
webpages[2][11] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-12-Half_Measures"
webpages[2][12] = "https://subslikescript.com/series/Breaking_Bad-903747/season-3/episode-13-Full_Measure"

# season 4
webpages[3][0] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-1-Box_Cutter"
webpages[3][1] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-2-Thirty-Eight_Snub"
webpages[3][2] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-3-Open_House"
webpages[3][3] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-4-Bullet_Points"
webpages[3][4] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-5-Shotgun"
webpages[3][5] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-6-Cornered"
webpages[3][6] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-7-Problem_Dog"
webpages[3][7] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-8-Hermanos"
webpages[3][8] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-9-Bug"
webpages[3][9] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-10-Salud"
webpages[3][10] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-11-Crawl_Space"
webpages[3][11] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-12-End_Times"
webpages[3][12] = "https://subslikescript.com/series/Breaking_Bad-903747/season-4/episode-13-Face_Off"

# season 5
webpages[4][0] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-1-Live_Free_or_Die"
webpages[4][1] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-2-Madrigal"
webpages[4][2] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-3-Hazard_Pay"
webpages[4][3] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-4-Fifty-One"
webpages[4][4] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-5-Dead_Freight"
webpages[4][5] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-6-Buyout"
webpages[4][6] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-7-Say_My_Name"
webpages[4][7] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-8-Gliding_Over_All"
webpages[4][8] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-9-Blood_Money"
webpages[4][9] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-10-Buried"
webpages[4][10] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-11-Confessions"
webpages[4][11] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-12-Rabid_Dog"
webpages[4][12] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-13-Tohajiilee"
webpages[4][13] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-14-Ozymandias"
webpages[4][14] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-15-Granite_State"
webpages[4][15] = "https://subslikescript.com/series/Breaking_Bad-903747/season-5/episode-16-Felina"

season = 1
episode = 1

for x in webpages:
    for y in x:
        print("Searching S" + str(season) + "E" + str(episode) + "...")
        if y == "n":
            episode = episode + 1
            break
        try:
            page = requests.get(y).text
        except:
            print("Error - could not communicate with webpage.")

        print("Obtained page")
        page_soup = BeautifulSoup(page, "html.parser")

        script = page_soup.find('div',{'class':"full-script"})

        script = page_soup.get_text()

        script = script.split(" ")

        #script = page_soup.get_text()

        for z in script:
            if z == "Oh, ":
                print("SCREAM")
            for country in countryArr:
                if z == country:
                    print(country + " mentioned in S" + str(season) + "E" + str(episode))
        episode = episode + 1
    season = season + 1
    episode = 1


