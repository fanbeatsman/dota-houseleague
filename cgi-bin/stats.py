#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import cgi
import cgitb
import os
import unirest
import json
import requests
#qweqweeqw
response = unirest.get("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=E8CF984D05F34C0CA6BE2A5ED5639FA0")
 

r=requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")
r.text
data=json.loads(r.text)


s = None
form_error = 0
con = None
SQL_error = None
try:
	form = cgi.FieldStorage()
	win = form["1wins"].value.strip('\n')
	num_players = int(form["num_players"].value)
		
#	s = cgi.escape(form) weird stuff here, might come back to it for adding security
except:
	form_error = 1



if (form_error == 0):
	try:
		con = lite.connect('/var/www/data/stats.db')
		con.row_factory = lite.Row
		cur = con.cursor()
		i = 1
		rollback = 0
		while (i <= num_players):
			
			win = int(form["%dwins" %i].value) 
			player_name = form["%dname" %i].value
			kills = int(form["%dkills" %i].value) 
			deaths = int(form["%ddeaths" %i].value)

			cur.execute("SELECT EXISTS(SELECT * FROM Players WHERE Name=?)", (player_name,))

			if (int(cur.fetchone()[0]) == 0):
				rollback=rollback+1
			#wins AND loses update		
			if (win == 1):
				cur.execute("UPDATE Players SET Wins=Wins+1 WHERE Name=?", (player_name,))
			else:
				cur.execute("UPDATE Players SET Loses=Loses+1 WHERE Name=?", (player_name,))

			#kills updates
			cur.execute("UPDATE Players SET Kills=Kills+? WHERE Name=?", (kills, player_name))
			
			#deaths updates
			cur.execute("UPDATE Players SET Deaths=Deaths+? WHERE Name=?", (deaths, player_name))
	
			i=i+1
		if rollback < 1:
			con.commit()
		else:
			con.rollback()


		con.commit()
	
	except lite.Error, e:
		SQL_error = e.args[0]
		if con:
			con.rollback()
	finally:
		if con:
			con.close()
con = lite.connect('/var/www/data/stats.db')

with con:
	
	con.row_factory = lite.Row 
	cur = con.cursor()   
	cur.execute("SELECT * FROM Players")
	
	rows = cur.fetchall()





try:
	players = open("players.ssv","r")
	lines = players.readlines()
except:
	print "Error in reading players"

print "Content-Type: text/html"
print
print
print '''<html>
	<head>
		<title>Stats</title>
		<link href="http://bushleague.x64.me/templatemo_400_polygon/css/mystyle.css" rel="stylesheet">
	</head>
	<body>
	<br><br><br><br><br>
	<center>
	<div class="responsive_menu">
                                <ul>
                                </ul>
                                           
	<h1>TESTING IN USR/LIb/CGI-BIN</h1>
	'''
'''i=0
while i < len(lines):
	printer = lines[i].strip('\n')
	print lines[i]

	print printer
	i=i+1
'''
print "# | Name | Wins | Loses | Kills | Deaths"
print "<br>"
for row in rows: 
		print "<br>"
		print "%s | %s | %s | %s | %s | %s<br>" % (row["Id"], row["Name"], row["Wins"], row["Loses"], row["Kills"], row["Deaths"])
print "<br><br><br>"
print response
for item in data['data']['items']:

    print "Video Title: %s<br>" % (item['title'])

    print "Video Category: %s<br>" % (item['category'])

    print "Video ID: %s<br>" % (item['id'])

    print "Video Rating: %f<br>" % (item['rating'])

    print "Embed URL: %s<br>" % (item['player']['default'])

    print"<br>"
print SQL_error
print '''
	</center>
	</body>
	
	
	</html>
	'''
