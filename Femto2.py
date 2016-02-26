import pygame, sys, glob

pygame.mixer.init()

print ('Welcome to PyFemto2 BETA 1, by ByteUp Software!')
print ('Please report any bugs to the GitHub repository.')
print ('Type a command, or "h" for a help screen.')

songPlaying = 0
playing = 'Nothing'

while True:

    print
    cmd = raw_input('femto2> ')

    if cmd == 'o':
        files = glob.glob('music\*.*')
        counter = 0

        for i in files:
            counter = counter + 1
            filename = str(counter) + '. ' + str(i)
            print filename

        songNumber = raw_input('Select a song number to start: ')

        try:
            songNumber = int(songNumber)
        except:
            print ('Please enter a valid number.')
            break

        try:
            playing = files[songNumber - 1]
        except:
            print ('Please enter a valid number.')
            break

        try:
            pygame.mixer.music.load(playing)
        except:
            print ('Sorry, but that file is not in a supported format.')
            break

        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        songPlaying = 1
        print ('Now Playing: ' + playing.upper())

        try:
            pygame.mixer.music.queue(files[songNumber])
        except:
            pygame.mixer.music.queue(files[songNumber - 1])

    if cmd == 'ps':
        if songPlaying == 1:
            pygame.mixer.music.pause()
            print ('Audio paused.')
            songPlaying == 0
        else:
            print ('No audio to pause at this time.')

    if cmd == 'up':
        if songPlaying == 0 and pygame.mixer.music.get_busy() == 0:
            pygame.mixer.music.unpause()
            print ('Audio unpaused.')
        else:
            print ('No audio to unpause at this time.')

    if cmd == 'st':
        if songPlaying == 1:
            pygame.mixer.music.stop()
            songPlaying == 0
            playing = 'Nothing'
        else:
            print ('No audio to stop at this time.')

    if cmd == 'vo':
        volume = pygame.mixer.music.get_volume() * 100
        print ('Current volume: ' + str(volume) + '%')
        newVolume = raw_input('New volume: ')
        try:
            newVolume = int(newVolume) / 100
        except:
            print ('Please enter a valid integer.')
            break

        if newVolume > 1:
            print ('Please enter a volume between 1 and 100.')
        elif newVolume < 0:
            print ('Please enter a volume between 1 and 100.')
        else:
            pygame.mixer.music.set_volume(newVolume)

    if cmd == 'np':
        print ('Now Playing: ' + playing)

    if cmd == 'h':
        print ('COMMAND HELP')
        print ('o - open a file (type "x" and enter to cancel this)')
        print ('ps - pause audio currently playing')
        print ('up - unpause audio')
        print ('st - stop audio currently playing')
        print ('vo - change volume (accepts integers between 1 and 100)')
        print ('h - show this screen')
        print ('ex - exit the program')
        print
        print ('COMING SOON')
        print ('q - queue the next song(s)')
        print ('c - view credits')

    if cmd == 'ex':
        exit = raw_input('Are you sure you want to exit (Y/N)? ')
        if exit.upper() == 'Y':
            print ('Exiting...')

            try:
                pygame.music.mixer.stop()
            except:
                print ('No music playing.')

            sys.exit()
        elif exit.upper() != 'N':
            print ('Please enter either the letter Y or N.')
