@echo off
	title Femto Music Player v1.3
	color f0
	echo Welcome to Femto Music Player's Batch launcher!
	set/p showMusic= Do you want to see the music in the Femto folder? (Y/N) 
		if %showMusic% == Y goto displayFolder
		if %showMusic% == y goto displayFolder

		:load
			echo.
			echo Loading Femto Music Player...
			python Femto.py

		:displayFolder
			echo Music in Femto folder:
			echo.
			cd music
			dir
			cd ..
			goto load