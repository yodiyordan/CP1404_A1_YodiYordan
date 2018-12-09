"""
CP1404 Programming II - Assignment 1
Yodi Setiadi Yordan

This program will read a song file (Songs.csv) and allows the user to keep track of which songs they have learned
and which songs they have not learned. The user can add a new song to the list and choose what song they want to
complete.

https://github.com/yodiyordan/CP1404_A1_YodiYordan
"""

from operator import itemgetter

songs_file = "Songs.csv"
song_list = []


def main():
    open_file()  # read Songs.csv file
    print("Songs To Learn 1.0 - by Yodi Setiadi Yordan")
    total_songs = calculate_songs()  # calculate the number of songs in the csv file
    print("{} songs loaded".format(total_songs))
    while True:
        print("Menu :")
        print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        answer = input(">>> ")  # get user input
        answer = answer.upper()  # transform all letters to uppercase to handle both lowercase and uppercase letters
        answer = valid_check(answer)  # check whether the entered input is valid or not
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
        data = data.strip()  # delete the spaces in the csv file
        data = data.split(",")
        song_list.sort(key=itemgetter(1, 2))  # sort all the songs according to their artist then by their title
        song_list.append(data)  # append the arranged csv file (Songs.csv) to song_list
    file.close()


def calculate_songs():
    songs = 0
    for song in range(len(song_list)):
        songs += 1
    return songs


def valid_check(choice):
    while choice != "L" and choice != "A" and choice != "C" and choice != "Q":  # check if the user enters a valid input
        print("Invalid menu choice")
        print("Menu :")
        print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>> ")
        choice = choice.upper()  # transform all letters to uppercase to handle both lowercase and uppercase letters
    return choice


def list_song():
    songs_learned = 0
    songs_not_learned = 0
    for index, data in enumerate(song_list):  # arrange the spacing of song list
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
        if title == "":  # avoid the user from inserting a blank input
            print("Input can not be blank")
        else:
            break
    add_new_song.append(title)  # append the new song data (title) to add_new_song

    while True:
        artist = str(input("Artist: "))
        if artist == "":  # avoid the user from inserting a blank input
            print("Input can not be blank")
        else:
            break
    add_new_song.append(artist)  # append the new song data (artist) to add_new_song

    while True:
        try:
            year = int(input("Year: "))
            if year <= 0:  # ensure the user did not enter negative numbers
                print("Number must be >=0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")
    add_new_song.append(str(year))  # append the new song data (year) to add_new_song
    print("{} by {} ({}) added to song list".format(title, artist, year))
    add_new_song.append("y")  # mark the newly added song as not learned
    song_list.append(add_new_song)  # append the new song info (title, artist, year) to song_list
    song_list.sort(key=itemgetter(1, 2))  # sort all the songs according to their artist then by their title


def complete_song():
    number_complete = 0
    for complete in song_list:
        if complete[3] == "y":
            number_complete -= 1
    songs_amount = int(calculate_songs())  # calculate the number of songs at the moment
    if number_complete != 0:
        print("Enter the number of a song to mark as learned")
        while True:
            try:
                respond = int(input(">>> "))
                if respond >= songs_amount:  # check if the user enters a valid song number
                    print ("Invalid song number")
                elif respond < 0:  # ensure the user did not enter negative numbers
                    print ("Number must be >= 0")
                else:
                    break
            except ValueError:
                print("Invalid input; enter a valid number")
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
    file_save = open(songs_file, "w")  # clear the songs_file
    for song in song_list:
        new_song = "{},{},{},{}".format(song[0], song[1], song[2], song[3]) + "\n"
        file_save.write(new_song)  # save the new song to the csv file (Songs.csv)
    file_save.close()


main ()