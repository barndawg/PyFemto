import pygame, sys

next = 0
breakLoop = 0

print ("Femto v1.3: the tiny music player by ByteUp! Software.")

while True:

        print ("Type a command. Enter 'help' for a list of commands.")
        command = raw_input("> ")

        if command == "stop":
                print ("Stopping music...")
                try:
                        pygame.mixer.music.stop()
                except:
                        print ("No music playing at this time.")
                if next != 0:
                        command = "open"

        if command == "open":
                breakLoop = 0
                cancel = 0
                while breakLoop == 0:
                        if next == 0:
                                songname = raw_input ("Songname (e.g 'This Song'.) > ")
                                playing = songname.upper()
                                songname = ("music/" + songname)
                        else:
                                songname = next
                                next = 0

                        breakLoop = 1

                xmixer.init()
                breakLoop = 0
                extensionNum = 1
                loadFailed = 0

                while breakLoop == 0:
                        if extensionNum == 1:
                                songfile = songname + ".mp3"
                        if extensionNum == 2:
                                songfile = songname + ".wav"
                        if extensionNum == 3:
                                songfile = songname + ".ogg"
                        if extensionNum == 4:
                                print ("It looks like the song file: '" + playing + "' you typed in either doesn't exist, or isn't in a supported file format! Additionally, the file may be corrupted...")
                                loadFailed = 1
                                breakLoop = 1

                        try:
                                pygame.mixer.music.load(songfile)
                                breakLoop = 1

                        except:
                                extensionNum = extensionNum + 1

                if loadFailed == 0:
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(1)
                        print ("Now Playing: " + playing)


        elif command == "help":
            print ("List of commands")
            print ("help - Show this screen.")
            print ("open - Open a file to play music from.")
            print ("stop - Stop playback.")
            print ("queue - Specify next song. NOTE: one song in queue at a time.")
            print ("pause - Pause playback, press [ENTER] to resume.")
            print ("lyrics - Displays lyrics for song, if any.")
            print ("exit - Exits the program.")
            print ("credits - Shows credits.")
            print ("version - Shows the version of the player.")
            print ("changelog - Show a changelog.")

        elif command == "lyrics":
            breakLoop = 0

            while breakLoop == 0:
                lyrics = raw_input("Lyrics filename (has to be .txt)> ")
                lyrics = ("lyrics/" + lyrics + ".txt")

                breakLoop = 1

                try:
                    lyricFile = open(lyrics , 'r')

                except:
                    print ("Looks like the filename you just entered doesn't exist.")
                    breakLoop = "0"

            print
            print lyricFile.read()

        elif command == "queue":
            next = raw_input("Songname (e.g 'This Song'.) > ")
            playing = next
            next = ("music/" + next)

        elif command == "pause":
            pygame.mixer.music.pause()
            raw_input ("Press [ENTER] to resume playback.")
            pygame.mixer.music.unpause()

        elif command == "credits":
            print ("Credits")
            print ("Barney Watson - Coding")
            print ("Explora Albuquerque - Coding help (Programmable Pi Course)")

        elif command == "version":
            print ("Version")
            print ("Femto Music Player v1.3")
            print ("Last updated 25/03/2015")

        elif command == "changelog":
            print ("Changelog")
            print ("v1.0: Initial release.")
            print ("v1.1: Added more commands: changelog and version, and polished up UI in general. Added a 'command doesn't exist' function, deleted redundant 'next' command, renamed 'add' command to 'queue'.")
            print ("v1.2: No need to write file extension for song name any more, automatically tries all supported extensions. Slightly edited UI to incorporate this. Slightly changed batch version too...")
            print ("v1.3: Commands can now be used without playing a file. Use the 'open' command to open a file. Bug fixes, tweaks, and slight launcher (both bash and batch) tweaks too...")
            print ("v1.4: Work in progress, this update might bring changes to the help screen.")

        elif command == "exit":
            try:
                    pygame.mixer.music.pause()
                    musicPlaying = 1
            except:
                    musicPlaying = 0
            print ("Exit")
            exit = raw_input("Do you want to exit? (Y/N) > ")
            if exit == "Y" or exit == "y":
                print ("Exiting...")
                sys.exit()
            else:
                if musicPlaying == 0:
                        print ("Not exiting.")
                else:
                        print ("Not exiting, resuming music...")
                pygame.mixer.music.unpause()

        else:
            if breakLoop != 1:
                print ("Oops: that command doesn't exist. Check your spelling, or type 'help' for a list of commands.")
