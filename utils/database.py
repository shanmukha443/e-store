# Database Utility Functions

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to database successfully.")
    except Error as e:
        print(e) 
    return conn


def close_connection(conn):
    """ close the database connection """
    if conn:
        conn.close()
        print("Connection closed.")


def execute_query(conn, query):
    """ Execute a single query """
    try:
        c = conn.cursor()
        c.execute(query)
        print("Query executed successfully.")
    except Error as e:
        print(e)


def fetch_all_records(conn, query):
    """ Fetch all records from the database """
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()  

