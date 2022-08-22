import random


for i in range(666):
    genres = "genres.txt"
    stilo = "styles.txt"
    years = "years.txt"
    comp = "comp.txt"

    genreWORDS = open(genres).read().splitlines()
    stiloWORDS = open(stilo).read().splitlines()
    yearsWORDS = open(years).read().splitlines()
    compWORDS = open(comp).read().splitlines()


    word1 =  random.choice(yearsWORDS) + ' ' + random.choice(genreWORDS) + ' ' + random.choice(compWORDS)


    with open("final.txt", "a+") as file_object:
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        # Append text at the end of filess
        file_object.write(word1)

