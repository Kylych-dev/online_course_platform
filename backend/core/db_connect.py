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





# github_url = 'https://api.github.com/search/repositories'

# # Зависимость для сортировки репозиториев
# def get_sort_by(sort_by: str = Query("stars", description="Field to sort by")):
#     if sort_by == 'stars':
#         return 'stargazers_count'
#     return sort_by

# params = {
#     'q': 'is:public',
#     'order': 'desc',
#     'per_page': 10
# }

# def get_github_repositories(params):
#     response = requests.get('https://api.github.com/search/repositories', params=params)
#     if response.status_code == 200:
#         return response.json()['items']
#     else:
#         print(f'Error {response.status_code}')
#         return None

# def format_repository(repo):
#     return f"{repo['name']} - {repo['stargazers_count']} stars"

# """
#     Получение списка репозиториев GitHub.

#     Args:
#         params (dict): Параметры запроса к API GitHub.

#     Returns:
#         list: Список отформатированных репозиториев или словарь с сообщением об ошибке.
# """
# def top_test(params):
#     repositories = get_github_repositories(params)
#     if repositories:
#         return repositories
#     else:
#         return {'error': 'Failed to fetch repositories'}






def insert_repository(repo_data, word1=None):
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_SERVER'),
        port=os.getenv('POSTGRES_PORT')
    )
    cur = conn.cursor()

    try:
        sql_query = f"INSERT INTO repositories ({word1}) VALUES (%s)"
        cur.execute(sql_query, repo_data)
        conn.commit()
        print("Data inserted successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting data:", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Database connection closed.")



def insert_repository2(repo_data):
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_SERVER'),
        port=os.getenv('POSTGRES_PORT')
    )
    cur = conn.cursor()

    try:
        sql_query = "INSERT INTO repositories (language, forks) VALUES (%s, %s)"
        cur.execute(sql_query, repo_data)
        conn.commit()
        print("Data inserted successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting data:", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Database connection closed.")


def insert_owner(owner_data):
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_SERVER'),
        port=os.getenv('POSTGRES_PORT')
    )
    cur = conn.cursor()

    try:
        sql_query = "INSERT INTO owners (name, repo_count) VALUES (%s, %s)"
        cur.execute(sql_query, owner_data)
        conn.commit()
        print("Data inserted successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting data:", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Database connection closed.")


def insert_stars(stars_data):
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_SERVER'),
        port=os.getenv('POSTGRES_PORT')
    )
    cur = conn.cursor()

    try:
        sql_query = "INSERT INTO stars (repo_name, stars) VALUES (%s, %s)"
        cur.execute(sql_query, stars_data)
        conn.commit()
        print("Data inserted successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting data:", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Database connection closed.")


def insert_data(table_name, data):
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_SERVER'),
        port=os.getenv('POSTGRES_PORT')
    )
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





#____________________________________________________________________________________
# import psycopg2
# from dotenv import load_dotenv
# from utils import get_github_repositories
# import os




# import psycopg2
# import os
# from dotenv import load_dotenv
# import requests
# from fastapi import FastAPI, HTTPException, Query


# load_dotenv()




# github_url = 'https://api.github.com/search/repositories'

# # Зависимость для сортировки репозиториев
# def get_sort_by(sort_by: str = Query("stars", description="Field to sort by")):
#     if sort_by == 'stars':
#         return 'stargazers_count'
#     return sort_by

# params = {
#     'q': 'is:public',
#     'order': 'desc',
#     'per_page': 10
# }

# def get_github_repositories(params):
#     response = requests.get('https://api.github.com/search/repositories', params=params)
#     if response.status_code == 200:
#         return response.json()['items']
#     else:
#         print(f'Error {response.status_code}')
#         return None

# def format_repository(repo):
#     return f"{repo['name']} - {repo['stargazers_count']} stars"

# """
#     Получение списка репозиториев GitHub.

#     Args:
#         params (dict): Параметры запроса к API GitHub.

#     Returns:
#         list: Список отформатированных репозиториев или словарь с сообщением об ошибке.
# """
# def top_test(params):
#     repositories = get_github_repositories(params)
#     if repositories:
#         return repositories
#     else:
#         return {'error': 'Failed to fetch repositories'}






# def insert_repository(repo_data, word1):
#     conn = psycopg2.connect(
#         dbname=os.getenv('POSTGRES_DB'),
#         user=os.getenv('POSTGRES_USER'),
#         password=os.getenv('POSTGRES_PASSWORD'),
#         host=os.getenv('POSTGRES_SERVER'),
#         port=os.getenv('POSTGRES_PORT')
#     )
#     cur = conn.cursor()

#     try:
#         sql_query = f"INSERT INTO repositories ({word1}) VALUES (%s)"
#         cur.execute(sql_query, repo_data)
#         conn.commit()
#         print("Data inserted successfully.")
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("Error while inserting data:", error)
#     finally:
#         if conn:
#             cur.close()
#             conn.close()
#             print("Database connection closed.")


#____________________________________________________________________________________



# @app.get("/top_language/{language}")
# def top_test_language(language: str, sort_by: str = 'stars'):
#     params_language = params.copy()
#     params_language['q'] = f'language:{language} is:public'
#     params_language['sort'] = sort_by

#     # Получение списка репозиториев
#     repositories = top_test(params_language)

#     for repo in repositories:
#         if 'language' in repo:
#             repo_data = (repo['language'], ) 
#             insert_repository(repo_data, 'language')
#         else:
#             print("Error: Missing 'language' key in repository data")


#     return repositories






# load_dotenv()


# def insert_repository(repo_data, word1):
#     conn = psycopg2.connect(
#         dbname=os.getenv('POSTGRES_DB'),
#         user=os.getenv('POSTGRES_USER'),
#         password=os.getenv('POSTGRES_PASSWORD'),
#         host=os.getenv('POSTGRES_SERVER'),
#         port=os.getenv('POSTGRES_PORT')
#     )
#     cur = conn.cursor()

#     try:
#         sql_query = f"INSERT INTO repositories ({word1}) VALUES (%s)"
#         cur.execute(sql_query, repo_data)
#         conn.commit()
#         print("Data inserted successfully.")
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("Error while inserting data:", error)
#     finally:
#         if conn:
#             cur.close()
#             conn.close()
#             print("Database connection closed.")







# def get_db_connection():
#     conn = psycopg2.connect(
#         dbname=os.getenv('POSTGRES_DB'),
#         user=os.getenv('POSTGRES_USER'),
#         password=os.getenv('POSTGRES_PASSWORD'),
#         host=os.getenv('POSTGRES_SERVER'),
#         port=os.getenv('POSTGRES_PORT')
#     )
#     return conn



# def insert_repository(repo_data):
#     conn = psycopg2.connect(
#         dbname=os.getenv('POSTGRES_DB'),
#         user=os.getenv('POSTGRES_USER'),
#         password=os.getenv('POSTGRES_PASSWORD'),
#         host=os.getenv('POSTGRES_SERVER'),
#         port=os.getenv('POSTGRES_PORT')
#     )
#     cur = conn.cursor()

#     sql_query = "INSERT INTO repositories (repo, owner, position_cur, position_prev, stars, watchers, forks, open_issues, language) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     cur.execute(sql_query, repo_data)
    
#     conn.commit()
#     cur.close()
#     conn.close()




# def parse_and_save_repositories():
#     params = {
#         'q': 'is:public',
#         'order': 'desc',
#         'per_page': 100
#     }
#     repositories = get_github_repositories(params)
#     for repo in repositories:
#         repo_data = (
#             repo['full_name'],
#             repo['owner']['login'],
#             repo['stargazers_count'],
#             repo['watchers_count'],
#             repo['forks_count'],
#             repo['open_issues_count'],
#             repo['language']
#         )
#         insert_repository(repo_data)






'''
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=postgres

'''