from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import requests

from db_connection import get_db_connection
from psycopg2 import sql

from datetime import datetime
from typing import List

app = FastAPI()



par = {
        'q': 'is:public',
        'order': 'desc', 
        'per_page': 100    
    }

github_url = 'https://api.github.com/search/repositories'

# Зависимость для сортировки репозиториев
def get_sort_by(sort_by: str = Query("stars", description="Field to sort by")):
    if sort_by == 'stars':
        return 'stargazers_count'
    return sort_by


# Пример эндпоинта для получения данных из таблицы
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = sql.SQL("SELECT * FROM items WHERE id = %s")
    cursor.execute(query, (item_id,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": item}



# эндпоинт для создания новой записи в таблице
@app.post("/items/")
async def create_item(name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = sql.SQL("INSERT INTO items (name) VALUES (%s) RETURNING id")
    cursor.execute(query, (name,))
    new_item_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return {"id": new_item_id, "name": name}





'''
http://127.0.0.1:8000/api/rep_100?sort_by=stars

Также можно попробовать другие поля для сортировки, например watchers, forks, open_issues, и т.д.

arduino

http://127.0.0.1:8000/api/rep_100?sort_by=watchers

arduino

http://127.0.0.1:8000/api/rep_100?sort_by=forks



arams = {
    'q': 'is:public',
    'order': 'desc',  # Убывающий порядок
    'per_page': 5   # Количество результатов на страницу
    }


    Код выглядит хорошо и эффективно написан. Он содержит несколько конечных точек, каждая из которых обращается к API GitHub для получения информации о репозиториях, а затем форматирует результаты и возвращает их пользователю.

Вот несколько возможных улучшений:

    Повторяющийся код: В конечных точках top_repo, top_owner и top_stars происходит дублирование логики создания параметров запроса и вызова make_github_request(). Можно было бы вынести эту общую логику в отдельную функцию, чтобы избежать повторения кода.

    Обработка ошибок: В текущей реализации кода отсутствует обработка ошибок, возникающих при выполнении запросов к API GitHub. Было бы полезно добавить обработку таких ситуаций, чтобы возвращать сообщение об ошибке клиенту, если запрос завершается неудачно.

    Документация: Добавление документации к конечным точкам поможет пользователям понять, как использовать ваше API. Вы можете добавить описания параметров и ожидаемых результатов для каждой конечной точки.

    Поддержка сортировки по различным полям: Ваш код в настоящее время поддерживает сортировку только по звездам ('stars'). Было бы полезно добавить поддержку сортировки по другим полям, таким как количество форков, дата обновления и т. д.

В целом, ваш код кажется хорошо структурированным и эффективным, и эти улучшения могут сделать его еще лучше.


2024-01-01 2024-01-31


'''



params = {
    'q': 'is:public',
    'order': 'desc',
    'per_page': 10
}

def get_github_repositories(params):
    response = requests.get('https://api.github.com/search/repositories', params=params)
    if response.status_code == 200:
        return response.json()['items']
    else:
        print(f'Error {response.status_code}')
        return None

def format_repository(repo):
    return f"{repo['name']} - {repo['stargazers_count']} stars"

"""
    Получение списка репозиториев GitHub.

    Args:
        params (dict): Параметры запроса к API GitHub.

    Returns:
        list: Список отформатированных репозиториев или словарь с сообщением об ошибке.
"""
def top_test(params):
    repositories = get_github_repositories(params)
    if repositories:
        formatted_repositories = [format_repository(repo) for repo in repositories]
        return formatted_repositories
    else:
        return {'error': 'Failed to fetch repositories'}

@app.get("/top_language/{language}")
def top_test_language(language: str, sort_by: str = 'stars'):
    params_language = params.copy()
    params_language['q'] = f'language:{language} is:public'
    params_language['sort'] = sort_by
    return top_test(params_language)

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




# Пример общей логики для получения активности репозитория по коммитам за указанный промежуток времени
def get_repository_activity(owner: str, repo: str, since: datetime, until: datetime):
    # Здесь должен быть ваш код для получения активности репозитория по коммитам за указанный промежуток времени
    # Например, можно использовать API GitHub для этой цели
    # Примечание: Этот код должен быть реализован в соответствии с требованиями вашего проекта
    # Возвращаем заглушечные данные для демонстрации
    activity_data = [
        {"date": "2024-03-01", "commits": 3, "authors": ["author1", "author2"]},
        {"date": "2024-03-02", "commits": 5, "authors": ["author3", "author4"]},
        # Другие записи активности...
    ]
    return activity_data

# Функция для форматирования результата активности репозитория в соответствии с требуемой схемой
def format_repository_activity(activity_data: List[dict]):
    # Преобразуем объекты активности репозитория в соответствии с требуемой схемой
    formatted_data = []
    for entry in activity_data:
        formatted_entry = {
            "date": entry["date"],
            "commits": entry["commits"],
            "authors": entry["authors"]
        }
        formatted_data.append(formatted_entry)
    return formatted_data

# Конечная точка FastAPI для обработки запросов к /api/repos/{owner}/{repo}/activity
@app.get("/api/repos/{owner}/{repo}/activity")
async def get_repository_activity_endpoint(owner: str, repo: str, since: datetime, until: datetime):
    try:
        # Получаем активность репозитория
        activity_data = get_repository_activity(owner, repo, since, until)
        # Форматируем результат активности репозитория
        formatted_activity_data = format_repository_activity(activity_data)
        # Возвращаем отформатированные данные
        return formatted_activity_data
    except Exception as e:
        # Если возникает ошибка, возвращаем сообщение об ошибке с кодом HTTP 500
        raise HTTPException(status_code=500, detail=str(e))




'''



params = {
    'q': 'is:public',
    'order': 'desc',
    'per_page': 10
}



def get_github_repositories(params):
    response = requests.get('https://api.github.com/search/repositories', params=params)
    if response.status_code == 200:
        return response.json()['items']
    else:
        print(f'Error {response.status_code}')
        return None
    

def format_repository(repo):
    return f"{repo['name']} - {repo['stargazers_count']} stars"


@app.get("/top_language/{language}")
def top_test_language(language: str, sort_by: str = 'stars'):
    params_language = params.copy()
    params_language['q'] = f'language:{language} is:public'
    params_language['sort'] = sort_by
    
    repositories = get_github_repositories(params_language)
    if repositories:
        formatted_repositories = [format_repository(repo, sort_by) for repo in repositories]
        return formatted_repositories
    else:
        return []

@app.get("/top_repo/")
def top_repo(owner: str = None, sort_by: str = 'stars'):
    params_repo = params.copy()
    query = 'is:public'
    if owner:
        query += f' user:{owner}'
    params_repo['q'] = query
    params_repo['sort'] = sort_by
    
    repositories = get_github_repositories(params_repo)
    if repositories:
        formatted_repositories = [format_repository(repo) for repo in repositories]
        return formatted_repositories
    else:
        return []

@app.get("/top_owner/")
def top_owner(owner: str = None, sort_by: str = 'stars'):
    params_top = params.copy()
    query = 'is:public'
    if owner:
        query += f' user:{owner}'
    params_top['q'] = query
    params_top['sort'] = sort_by
    
    repositories = get_github_repositories(params_top)
    if repositories:
        formatted_repositories = [format_repository(repo) for repo in repositories]
        return formatted_repositories
    else:
        return []

@app.get("/top_stars")
def top_stars():
    params['sort'] = 'stars'
    repositories = get_github_repositories(params)
    if repositories:
        formatted_repositories = [format_repository(repo) for repo in repositories]
        return formatted_repositories
    else:
        return []

'''






































'''

params = {
    'q': 'is:public',
    'order': 'desc',
    'per_page': 10
}

def make_github_request(params):
    response = requests.get('https://api.github.com/search/repositories', params=params)
    if response.status_code == 200:
        return response.json()['items']
    else:
        print(f'Error {response.status_code}')
        return None
    

def format_repository(repo):
    return f"{repo['name']} - {repo['stargazers_count']} stars"


@app.get("/top_language/{language}")
def top_test_language(language: str, sort_by: str = 'stars'):
    params_language = params.copy()
    params_language['q'] = f'language:{language} is:public'
    params_language['sort'] = sort_by
    
    repositories = make_github_request(params_language)
    if repositories:
        formatted_repositories = [format_repository(repo, sort_by) for repo in repositories]
        return formatted_repositories
    else:
        return []

@app.get("/top_repo/")
def top_repo(owner: str = None, sort_by: str = 'stars'):
    params_repo = params.copy()
    query = 'is:public'
    if owner:
        query += f' user:{owner}'
    params_repo['q'] = query
    params_repo['sort'] = sort_by
    
    repositories = make_github_request(params_repo)
    if repositories:
        formatted_repositories = [format_repository(repo) for repo in repositories]
        return formatted_repositories
    else:
        return []

@app.get("/top_owner/")
def top_owner(owner: str = None, sort_by: str = 'stars'):
    params_top = params.copy()
    query = 'is:public'
    if owner:
        query += f' user:{owner}'
    params_top['q'] = query
    params_top['sort'] = sort_by
    
    repositories = make_github_request(params_top)
    if repositories:
        formatted_repositories = [format_repository(repo) for repo in repositories]
        return formatted_repositories
    else:
        return []

@app.get("/top_stars")
def top_stars():
    params['sort'] = 'stars'
    repositories = make_github_request(params)
    if repositories:
        formatted_repositories = [format_repository(repo) for repo in repositories]
        return formatted_repositories
    else:
        return []
    
'''

'''
    repo: str           +
    owner: str          +
    position_cur: int
    position_prev: int
    stars: int          +
    watchers: int       +
    forks: int          +
    open_issues: int    +
    language: str       +

    
'''