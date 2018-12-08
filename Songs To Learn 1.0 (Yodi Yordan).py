"""
CP1404 Programming II Assignment 1
Yodi Setiadi Yordan
https://github.com/yodiyordan/CP1404_A1_YodiYordan
"""

from operator import itemgetter

songs_file = "Songs.csv"
song_list = []


def main():
    open_file()
    print("Songs To Learn 1.0 - by Yodi Setiadi Yordan")
    total_songs = calculate_songs()
    print("{} songs loaded".format(total_songs))
    while True:
        print("Menu :")
        print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        answer = input(">>> ")
        answer = answer.upper()
        answer = valid_check(answer)
        if answer == "L":
            list_song()
        if answer == "A":
            add_song()
        if answer == "C":
            complete_song()
        if answer == "Q":
            close_program()
            break
    print("Thank you, have a nice day :)")


def open_file():
    file = open(songs_file, "r")
    for data in file.readlines():
        data = data.strip()
        data = data.split(",")
        song_list.sort(key=itemgetter(1, 2))
        song_list.append(data)
    file.close()


def calculate_songs():
    songs = 0
    for song in range(len(song_list)):
        songs += 1
    return songs


def valid_check(choice):
    while choice != "L" and choice != "A" and choice != "C" and choice != "Q":
        print("Invalid menu choice")
        print("Menu :")
        print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>> ")
        choice = choice.upper()
    return choice


def list_song():
    songs_learned = 0
    songs_not_learned = 0
    for index, data in enumerate(song_list):
        if data[3] == "y":
            print(index, "* {:30s} - {:25s} ({})".format(data[0], data[1], data[2]))
            songs_not_learned += 1
        else:
            print(index, "  {:30s} - {:25s} ({})".format(data[0], data[1], data[2]))
            songs_learned += 1
    print("{} songs learned, {} songs still to learn".format(songs_learned, songs_not_learned))


def add_song():
    add_new_song = []
    while True:
        title = str(input("Title: "))
        if title == "":
            print("Input can not be blank")
        else:
            break
    add_new_song.append(title)

    while True:
        artist = str(input("Artist: "))
        if artist == "":
            print("Input can not be blank")
        else:
            break
    add_new_song.append(artist)

    while True:
        try:
            year = int(input("Year: "))
            if year <= 0:
                print("Number must be >=0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")
    add_new_song.append(str(year))
    print("{} by {} ({}) added to song list".format(title, artist, year))
    add_new_song.append("y")
    song_list.append(add_new_song)
    song_list.sort(key=itemgetter(1, 2))


def complete_song():
    number_complete = 0
    for complete in song_list:
        if complete[3] == "y":
            number_complete -= 1
    songs_amount = int(calculate_songs())
    if number_complete != 0:
        print("Enter the number of a song to mark as learned")
        while True:
            try:
                respond = int(input(">>> "))
                if respond >= songs_amount:
                    print ("Invalid song number")
                elif respond < 0:
                    print ("Number must be >= 0")
                else:
                    break
            except ValueError:
                print("Invalid input; please enter a valid number")
        for index, data in enumerate(song_list):
            if index == respond:
                if data[3] == "y":
                    data[3] = "n"
                    print("{} by {} learned".format(data[0], data[1]))
                else:
                    print("You have already learned {}".format(data[0]))
    else:
        print("No more songs to learn!")


def close_program():
    calculate_songs()
    print("{} songs saved to Songs.csv".format(calculate_songs()))
    file_save = open(songs_file, "w")
    for song in song_list:
        new_song = "{},{},{},{}".format(song[0], song[1], song[2], song[3]) + "\n"
        file_save.write(new_song)
    file_save.close()


main()