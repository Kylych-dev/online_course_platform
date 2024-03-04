import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_database_connection():
    return psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_SERVER'),
        port=os.getenv('POSTGRES_PORT')
    )

'''
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='1'
POSTGRES_SERVER='localhost'
POSTGRES_PORT='5432'
POSTGRES_DB='postgres'

'''


def insert_data(table_name, data):
    conn = get_database_connection()
    cur = conn.cursor()

    try:
        sql_query = f"INSERT INTO {table_name} (repo_name, value) VALUES (%s, %s)"
        cur.execute(sql_query, data)
        conn.commit()
        print("Data inserted successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting data:", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Database connection closed.")


def insert_repository(repo_data, word1=None):
    table_name = 'repositories'
    insert_data(table_name, repo_data)


def insert_owner(owner_data):
    table_name = 'owners'
    insert_data(table_name, owner_data)


def insert_stars(stars_data):
    table_name = 'stars'
    insert_data(table_name, stars_data)


def insert_watchers(watchers_data):
    table_name = 'watchers'
    insert_data(table_name, watchers_data)


def insert_forks(forks_data):
    table_name = 'forks'
    insert_data(table_name, forks_data)


def insert_open_issues(open_issues_data):
    table_name = 'open_issues'
    insert_data(table_name, open_issues_data)

'''
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=postgres

'''