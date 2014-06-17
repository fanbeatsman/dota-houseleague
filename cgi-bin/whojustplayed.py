#!/usr/bin/env python

import sys
import os


try:
	get_players = open("players.ssv", "r")
	players = get_players.readlines()
	i=0
	while i < len(players):
		players[i] = players[i].strip()
		i=i+1
	
	get_players.close()
except:
	print "Error in reading players.ssv"
num_players = []
if (os.environ.get('QUERY_STRING')):
	query = os.environ.get('QUERY_STRING')
	query = query.split('=')
	num_players = query[1].strip('\n')
	
print  "Content-Type: text/html"
print
print
print '''<html>

        <head>
                <title> Add stats</title>
		<link href="http://bushleague.x64.me/templatemo_400_polygon/css/mystyle.css" rel="stylesheet">

        </head>
	<body>
                <br>

                <center>

		<h1>So You Just Played, now update the stats</h1>
		<h2>Enter the players who have played and their scores</h2>
		[player's nickname] [win] [kills] [deats] (write 1 in the second box if player won, 0 if lost)
		<form name = "game_players" action="stats.py" method="post">
'''
i=0
while i < int(float(num_players)):
	print "player %d: <input type=\"text\" name =\"%dname\"><input type=\"text\" name=\"%dwins\"> <input type=\"text\" name=\"%dkills\"> <input type=\"text\" name=\"%ddeaths\"><br>" %(i+1,i+1,i+1,i+1,i+1)
	i=i+1

print "<input type=\"hidden\" name=\"num_players\" value=\"%d\">" %int(float((num_players)))

print '''
		<input type="submit" value="Submit">

<!--		<div class="darken pic">
		<a href ='http://bushleague.x64.me/cgi-bin/joeysprogram.cgi'><img src="http://bushleague.x64.me/images/slark.jpg" alt="slark"></a>	
		<span class="imgDescription"><span><font size=5px>News</font></span></span>
		</div>
-->
	<center>

	</body>

	</html>
'''
