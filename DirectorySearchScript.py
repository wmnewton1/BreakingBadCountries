reader = open("C:/Users/Guest 1/OneDrive/Documents/Breaking Bad/All_countries.txt")
lines = reader.read()
reader.close()
countryArr = lines.split("\n")


for i in range(1,6):
    for j in range(1,17):
        reader = open("C:/Users/Guest 1/OneDrive/Documents/Breaking Bad/Subtitles/S" + str(i) + "E" + str(j) + ".txt")
        lines = reader.read()
        reader.close()
        if lines == "":
            break
        print("Searching S" + str(i) + "E" + str(j) + "...")
        lines = lines.replace(',', '')
        lines = lines.replace('?', '')
        lines = lines.replace('!', '')
        lines = lines.replace("\n", " ")
        lines = lines.replace('.', '')
        lines = lines.replace("'","")
        lines = lines.split(" ")

        writer = open("C:/Users/Guest 1/OneDrive/Documents/Breaking Bad/Countries mentioned.txt", 'a')

        for x in lines:
            if x == "Italian":
                writer.write("Italian mentioned in S" + str(i) + "E" + str(j) + "\n")
            for country in countryArr:
                if x == country:
                    writer.write(country + " mentioned in S" + str(i) + "E" + str(j) + "\n")


        writer.close()