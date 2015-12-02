==README==

Femto music player is (C) From The Byte Up Software 2014 - 2015. Femto was originally intended for the Raspberry Pi (I recommend the model B revision 2 for Femto), but feel free to use for any purposes. If you are going to adapt or change the music player, and make it available to download, please give me credit.

=INSTALLATION=

	WINDOWS
	
	Make sure you have both Python 2.7 and Pygame installed (https://www.python.org/downloads/)	(http://www.pygame.org/download.shtml)
	
	Then, double click on Femto.bat.
	
	You can also type in cmd "python Femto.py" (without the quotes).

	MAC

	See Linux.

	LINUX

	Skip this step if you have a Raspberry Pi running Raspbian:
	Make sure you have both Python 2.7 and Pygame installed (https://www.python.org/downloads/)	(http://www.pygame.org/download.shtml)


	The file named femto (not Femto.bat) is the Linux Femto "Launcher".
	It may not work immediately- you will need to change the permissions.
	Open up a command line window, and type in "chmod +x femto" (without the quotes), then press enter. Note 		that you will have to be in the Femto folder to do this. If you are not the superuser, you will 		need to type "sudo chmod +x femto".
	If you have done this correctly, there shouldn't be any errors.
	Now, you can type ./femto into the terminal to run Femto (please note you have to be in the Femto folder 			to do this).

	Alternatively, you can type "python Femto.py" into the terminal to run Femto (without the quotes).

==PLAYING MUSIC==
	
	Firstly, put all the music you want to play using Femto in the Music folder inside the Femto folder (for 	instance, C:/Users/ByteUp/Femto/Music/ ).

	Then open Femto. Type the command "open". Type in the name of your song without the file extension - for 	example, if the song I wanted to play was called "Song.mp3", I would type in "Song". Femto automatically 	cycles through all the file extensions it can use. They are: mp3, ogg, and wav. Support for more file 	formats may come later.

==OTHER COMMANDS==
	
	This is a copy of the list that comes up if you type in the "help" command in Femto:

	help - Show this screen.
	open - Open a file to play music from.
	stop - Stop playback.
	queue - Specify next song. NOTE: one song in queue at a time.
	pause - Pause playback, press [ENTER] to resume.
	lyrics - Displays lyrics for song, if any.
	exit - Exits the program.
	credits - Shows credits.
	version - Shows the version of the player.
	changelog - Show a changelog.