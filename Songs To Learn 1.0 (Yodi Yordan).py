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
    print("{} songs successfully loaded".format(total_songs))
    while True:
        print("Menu :")
        print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        answer = input(">>> ")


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


main()
