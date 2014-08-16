import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

db = "usage.db"

def get_webpage_content(url):
	webpage = requests.get(url)

	return webpage.content

def get_usage():
	c = get_webpage_content("https://www.start.ca/support/usage")
	soup = BeautifulSoup(c)

	for item in soup.find_all('div', class_ = 'content'):
		inner_div = str(item.div.li.get_text()).split()

	return inner_div[0]

def init_db(db):
	db_con = sqlite3.connect(db)
	print("opened db")
	sql = """
			CREATE TABLE usage_hist (
			id integer primary key autoincrement,
			usage string not null,
			dt datetime default current_timestamp
			);
		"""
	try:
		with db_con:	
			db_con.execute(sql)
	except:
		pass


def insert_usage(database, usage):
	db_con = sqlite3.connect(database)
	db_con.execute("INSERT INTO usage_hist (usage, dt) VALUES (?, ?)", [usage, datetime.now()])
	db_con.commit()

def print_entries(database):
	db_con = sqlite3.connect(database)
	
	with db_con:
		for row in db_con.execute("SELECT usage, dt FROM usage_hist"):
			print(row)

def list_entries(database):
	db_con = sqlite3.connect(database)
	usage_gb = []
	date = []

	with db_con:
		for row in db_con.execute("SELECT usage, dt FROM usage_hist"):
			usage_gb.append(row[0])
			date.append(row[1])
	return usage_gb, date

usage = get_usage()
insert_usage(db, usage)
print(get_usage())
print_entries(db)
print(list_entries(db))