from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

import db_connect as db
from psycopg2 import sql
import requests


from datetime import datetime
from typing import List
from utils import params, top_test



app = FastAPI()



@app.get("/top_language/{language}")
def top_test_language(language: str, sort_by: str = 'stars'):
    params_language = params.copy()
    params_language['q'] = f'language:{language} is:public'
    params_language['sort'] = sort_by

    # Получение списка репозиториев
    repositories = top_test(params_language)

    # Запись репозиториев в базу данных
    for repo in repositories:
        if 'language' in repo:
            repo_data = (repo['language'], ) 
            db.insert_repository(repo_data, 'language')
        else:
            print("Error: Missing 'language' key in repository data")

    return repositories

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
        repo_data = (repo['name'], repo['stargazers_count'])  # Предположим, что здесь 'name' и 'stargazers_count' - это нужные данные
        db.insert_repository(repo_data)
    
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

    # Запись данных в базу данных
    for repo in repositories:
        owner_data = (repo['owner']['login'], )  # здесь 'owner' и 'login' - это нужные данные
        db.insert_owner(owner_data)
    
    return repositories

@app.get("/top_stars")
def top_stars():
    params['sort'] = 'stars'
    repositories = top_test(params)

    # Запись данных в базу данных
    for repo in repositories:
        stars_data = (repo['name'], repo['stargazers_count'])  # здесь 'name' и 'stargazers_count' - это нужные данные
        db.insert_stars(stars_data)
    
    return repositories

@app.get("/top_watchers")
def top_watchers():
    params['sort'] = 'watchers'
    repositories = top_test(params)

    # Запись данных в базу данных
    for repo in repositories:
        watchers_data = (repo['name'], repo['watchers_count'])  # здесь 'name' и 'watchers_count' - это нужные данные
        db.insert_watchers(watchers_data)
    
    return repositories

@app.get("/top_forks")
def top_forks():
    params['sort'] = 'forks'
    repositories = top_test(params)

    # Запись данных в базу данных
    for repo in repositories:
        forks_data = (repo['name'], repo['forks_count'])  # здесь 'name' и 'forks_count' - это нужные данные
        db.insert_forks(forks_data)
    
    return repositories

@app.get("/top_open_issues")
def top_open_issues():
    params['sort'] = 'open_issues'
    repositories = top_test(params)

    # Запись данных в базу данных
    for repo in repositories:
        open_issues_data = (repo['name'], repo['open_issues_count'])  # здесь 'name' и 'open_issues_count' - это нужные данные
        db.insert_open_issues(open_issues_data)
    
    return repositories


'''
owner = 'Kylych-dev'
repo = 'reviro_test'
since = '2024-02-01T00:00:00Z'  # Начальная дата и время в формате ISO 8601
until = '2024-03-01T00:00:00Z'  # Конечная дата и время в формате ISO 8601

'''