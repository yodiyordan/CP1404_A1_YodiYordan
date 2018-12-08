"""
CP1404 Programming II Assignment 1
Yodi Setiadi Yordan
https://github.com/yodiyordan/CP1404_A1_YodiYordan/blob/master/Songs%20To%20Learn%201.0%20(Yodi%20Yordan).py
"""

from operator import itemgetter

data_sort = []
songs_file = "Songs.csv"


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


def open_file():
    file = open(songs_file, "r")
    for data in file.readlines():
        data = data.strip()
        data = data.split(",")
        data_sort.sort(key=itemgetter(1, 2))
        data_sort.append(data)
    file.close()


def calculate_songs():
    songs = 0
    for song in range(len(data_sort)):
        songs += 1
    return songs


def valid_check(choice):
    while choice != "L" and choice != "A" and choice != "C" and choice != "Q":
        print("Invalid input, please enter a valid input (L, C, A or Q)")
        print("Menu :")
        print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>> ")
        choice = choice.upper()
    return choice


def list_song():
    songs_learned = 0
    songs_not_learned = 0
    for index, data in enumerate(data_sort):
        if data[3] == "y":
            print(index, "* {:30s} - {:25s} ({})".format(data[0], data[1], data[2]))
            songs_not_learned += 1
        else:
            print(index, "  {:30s} - {:25s} ({})".format(data[0], data[1], data[2]))
            songs_learned += 1
    print("{} songs learned, {} songs still need to be learned".format(songs_learned, songs_not_learned))


main()