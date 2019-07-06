# filesorting
Frame sorting to easier managing and locating missing frames


Program to go through a list of images inside a directory and to sort them by spotting any missing frame image.

(e.g) > ls
	sd_fx29.0101.jpg	sd_fx29.0102.jpg	sd_fx29.0104.jpg	info.txt



it would return 

2 test.%04d.jpg 101-102
1 test.%04d.jpg 104-104
1 info.txt


The program is written in such a way that we can run over any Linux working directory and it would sort its components. I've incorporated a basic naming convention and it can be re-written to work for any naming convetions.  
