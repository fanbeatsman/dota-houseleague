#!/usr/bin/env python


try:
	get_players = open ("players.ssv", "r")
	players = get_players.readlines()
except:
	print "Error in reading players.ssv"


print  "Content-Type: text/html"
print
print
print '''<html>

        <head>

                <title> Add stats</title>
        </head>
                <br>

                <center>

		<h1>So You Just Played, now update the stats</h1>
'''


