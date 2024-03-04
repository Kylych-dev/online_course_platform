from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from .db_connect import insert_repository, insert_repository2, insert_owner, insert_stars
from psycopg2 import sql
import requests


from datetime import datetime
from typing import List
from .utils import params, top_test



app = FastAPI()





@app.get("/top_language/{language}")
def top_test_language(language: str, sort_by: str = 'stars'):
    params_language = params.copy()
    params_language['q'] = f'language:{language} is:public'
    params_language['sort'] = sort_by

    # Получение списка репозиториев
    repositories = top_test(params_language)

    for repo in repositories:
        if 'language' in repo:
            repo_data = (repo['language'], ) 
            insert_repository(repo_data, 'language')
        else:
            print("Error: Missing 'language' key in repository data")


    return repositories


# ________________________________________________________________

# @app.get("/top_repo/")
# def top_repo(owner: str = None, sort_by: str = 'stars'):
#     params_repo = params.copy()
#     query = 'is:public'
#     if owner:
#         query += f' user:{owner}'
#     params_repo['q'] = query
#     params_repo['sort'] = sort_by
    
#     # Получение списка репозиториев
#     repositories = top_test(params_repo)

#     # Запись репозиториев в базу данных
#     for repo in repositories:
#         if 'name' in repo and 'owner' in repo and 'stars' in repo and 'watchers' in repo and 'forks' in repo and 'open_issues' in repo and 'language' in repo:
#             repo_data = (repo['name'], repo['owner'], repo['stars'], repo['watchers'], repo['forks'], repo['open_issues'], repo['language'])
#             insert_repository(repo_data)
#         else:
#             print("Error: Missing key(s) in repository data")
    
#     return repositories
# ________________________________________________________________



# @app.get("/top_language/{language}")
# def top_test_language(language: str, sort_by: str = 'stars'):
#     params_language = params.copy()
#     params_language['q'] = f'language:{language} is:public'
#     params_language['sort'] = sort_by

#     # Получение списка репозиториев и их форматирование
#     repositories = top_test(params_language)

#     # Здесь можно вставить данные в базу данных для каждого репозитория
#     for repo in repositories:
#         repo_data = (repo['name'], repo['owner'], repo['position_cur'], repo['position_prev'], repo['stars'], repo['watchers'], repo['forks'], repo['language'])
#         insert_repository(repo_data)

#     return repositories




# ________________________________________________________________
# @app.get("/top_language/{language}")
# def top_test_language(language: str, sort_by: str = 'stars'):
#     params_language = params.copy()
#     params_language['q'] = f'language:{language} is:public'
#     params_language['sort'] = sort_by
#     return top_test(params_language)
# ________________________________________________________________



@app.get("/top_repo/")
def top_repo(owner: str = None, sort_by: str = 'stars'):
    params_repo = params.copy()
    query = 'is:public'
    if owner:
        query += f' user:{owner}'
    params_repo['q'] = query
    params_repo['sort'] = sort_by

    # Получение списка репозиториев
    repositories = top_test(params_repo)

    # Запись репозиториев в базу данных
    for repo in repositories:
        if 'language' in repo and 'forks' in repo:
            repo_data = (repo['language'], repo['forks'])
            insert_repository2(repo_data)
        else:
            print("Error: Missing 'language' or 'forks' key in repository data")

    return repositories



@app.get("/top_owner/")
def top_owner(owner: str = None, sort_by: str = 'stars'):
    params_top = params.copy()
    query = 'is:public'
    if owner:
        query += f' user:{owner}'
    params_top['q'] = query
    params_top['sort'] = sort_by

    # Получение списка репозиториев
    repositories = top_test(params_top)

    # Подсчет количества репозиториев для каждого владельца
    owner_counts = {}
    for repo in repositories:
        owner = repo.get('owner', {}).get('login')  # Получаем имя владельца
        owner_counts[owner] = owner_counts.get(owner, 0) + 1

    # Запись данных в базу данных
    for owner, count in owner_counts.items():
        owner_data = (owner, count)
        insert_owner(owner_data)

    return owner_counts


@app.get("/top_stars/")
def top_stars():
    params_top = params.copy()
    params_top['sort'] = 'stars'

    # Получение списка репозиториев
    repositories = top_test(params_top)

    # Запись данных в базу данных
    for repo in repositories:
        repo_name = repo.get('name')
        stars = repo.get('stargazers_count')
        stars_data = (repo_name, stars)
        insert_stars(stars_data)

    return repositories


# ________________________________________________________________







'''

@app.get("/top_repo/")
def top_repo(owner: str = None, sort_by: str = 'stars'):
    params_repo = params.copy()
    query = 'is:public'
    if owner:
        query += f' user:{owner}'
    params_repo['q'] = query
    params_repo['sort'] = sort_by
    return top_test(params_repo)

@app.get("/top_owner/")
def top_owner(owner: str = None, sort_by: str = 'stars'):
    params_top = params.copy()
    query = 'is:public'
    if owner:
        query += f' user:{owner}'
    params_top['q'] = query
    params_top['sort'] = sort_by
    return top_test(params_top)

@app.get("/top_stars")
def top_stars():
    params['sort'] = 'stars'
    return top_test(params)

@app.get("/top_watchers")
def top_watchers():
    params['sort'] = 'watchers'
    return top_test(params)

@app.get("/top_forks")
def top_forks():
    params['sort'] = 'forks'
    return top_test(params)

@app.get("/top_open_issues")
def top_open_issues():
    params['sort'] = 'open_issues'
    return top_test(params)


def get_commit_activity(owner, repo, since, until):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'since': since, 'until': until}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        commit_activity = {}
        for commit in commits:
            commit_date = commit['commit']['author']['date'][:10]  # extracting only date part
            commit_activity[commit_date] = commit_activity.get(commit_date, 0) + 1
        return commit_activity
    else:
        return None

@app.get("/api/repos/{owner}/{repo}/activity")
def repo_activity(owner: str, repo: str, since: str = None, until: str = None):
    # Default to one year period if 'since' and 'until' are not provided
    if since is None or until is None:
        since = '2023-03-01T00:00:00Z'
        until = '2024-03-01T00:00:00Z'
        
    # Call the function to get commit activity
    commit_activity = get_commit_activity(owner, repo, since, until)
    
    if commit_activity:
        return commit_activity
    else:
        return {"error": "Failed to fetch commit activity"}

'''

'''
owner = 'Kylych-dev'
repo = 'reviro_test'
since = '2024-02-01T00:00:00Z'  # Начальная дата и время в формате ISO 8601
until = '2024-03-01T00:00:00Z'  # Конечная дата и время в формате ISO 8601

'''