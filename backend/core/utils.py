import requests
from fastapi import FastAPI, HTTPException, Query



github_url = 'https://api.github.com/search/repositories'

# Зависимость для сортировки репозиториев
def get_sort_by(sort_by: str = Query("stars", description="Field to sort by")):
    if sort_by == 'stars':
        return 'stargazers_count'
    return sort_by

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
# def top_test(params):
#     repositories = get_github_repositories(params)
#     if repositories:
#         formatted_repositories = [format_repository(repo) for repo in repositories]
#         return formatted_repositories
#     else:
#         return {'error': 'Failed to fetch repositories'}


def top_test(params):
    repositories = get_github_repositories(params)
    if repositories:
        return repositories
    else:
        return {'error': 'Failed to fetch repositories'}
    


# def top_test(params):
#     repositories = get_github_repositories(params)
#     if repositories:
#         for repo in repositories:
#             if all(key in repo for key in ('name', 'owner', 'stars', 'watchers', 'forks', 'open_issues', 'language')):
#                 continue
#             else:
#                 print(f"Error: Missing key(s) in repository data: {repo}")
#         return repositories
#     else:
#         return {'error': 'Failed to fetch repositories'}

    


# def top_test(params):
#     repositories = get_github_repositories(params)
#     if repositories:
#         formatted_repositories = []
#         for repo in repositories:
#             if 'name' in repo and 'owner' in repo and 'stars' in repo and 'watchers' in repo and 'forks' in repo and 'open_issues' in repo and 'language' in repo:
#                 formatted_repositories.append(repo)
#             else:
#                 print("Missing key(s) in repository data:", repo)
#         return formatted_repositories
#     else:
#         return {'error': 'Failed to fetch repositories'}