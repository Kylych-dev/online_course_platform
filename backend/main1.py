import requests


# Модель данных для репозиториев

'''

class RepoItem(BaseModel):
    repo: str
    owner: str          +
    position_cur: int
    position_prev: int
    stars: int          +
    watchers: int       +
    forks: int          +
    open_issues: int    +
    language: str       +

    
'''





# ______________________________________________________
# def get_top_github(sort_by):
#     params = {
#         'q': 'is:public',
#         'sort': sort_by,
#         'order': 'desc', 
#         'per_page': 10    
#     }

#     response = requests.get('https://api.github.com/search/repositories', params=params)

#     if response.status_code == 200:
#         data = response.json()
#         repositories = data['items']

#         for index, repo in enumerate(repositories, start=1):
#             # Получаем дополнительную информацию о репозитории, включая язык программирования
#             repo_response = requests.get(repo['url'])
#             if repo_response.status_code == 200:
#                 repo_data = repo_response.json()
#                 language = repo_data.get('language', 'Unknown')
#                 print(f'{index}, {repo["name"]} - {language}')




def get_top_github(sort_by):
    params = {
        'q': 'is:public',
        # 'sort': sort_by,
        'order': 'desc', 
        'per_page': 10    
    }

    response = requests.get('https://api.github.com/search/repositories', params=params)

    if response.status_code == 200:
        data = response.json()

        # repositories = data['items']
        result = []

        repositories = data.get('items', [])
        for repo in repositories:
            repo_response = requests.get(repo['url'])
            if repo_response.status_code == 200:
                repo_data = repo_response.json()
                language = repo_data.get('language', 'Unknown')
                print(f'{repo["name"]} - {language}')

    # if response.status_code == 200:
    #     data = response.json()
    #     repositories = data['items']

    #     result = []
    #     for index, repo in enumerate(repositories, start=1):
    #         # Получаем дополнительную информацию о репозитории, включая язык программирования
    #         repo_response = requests.get(repo['url'])
    #         if repo_response.status_code == 200:
    #             repo_data = repo_response.json()
    #             language = repo_data.get('language', 'Unknown')
    #             # result.append(f'{index}, {repo["name"]} - {language}')
    #             result.append(language)

    return result


# ______________________________________________________
# Определить параметры запроса
# def get_top_github(sort_by):

#     if sort_by == 'stars':
#         sort_by = 'stargazers_count'

#     params = {
#         'q': 'is:public',
#         'sort': sort_by, 
#         # 'order': 'desc', 
#         # 'order': 'abc',   
#         'per_page': 10    
#     }

#     response = requests.get('https://api.github.com/search/repositories?q=is:public&sort=stars&per_page=100', params=params)

#     if response.status_code == 200:
#         data = response.json()
#         repositories = data['items']

#         for index, repo in enumerate(repositories, start=1):
#             print(f'{index} , {repo["name"]} - {repo[sort_by]} {sort_by}')
#     else:
#         print(f'Error {response.status_code}')
# ______________________________________________________


# print(get_top_github('language'))





'''
сортировки по полям в виде параметров запроса. 

API-приложение на FastAPI 
GET /api/repos/top100
Отображение топ 100 публичных репозиториев. Топ составляется по количеству звезд (stars). Плюсом будет реализация сортировки по полям в виде параметров запроса. 
Схема (список объектов):
    repo: string – название репозитория (full_name в API GitHub)
    owner: string - владелец репозитория
    position_cur: integer – текущая позиция в топе
    position_prev: integer – предыдущая позиция в топе
    stars: integer – количество звёзд
    watchers: integers – количество просмотров
    forks: integer – количество форков
    open_issues: integer – количество открытых issues
    language: string - язык

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



def get_repositories_by_language(language, sort_by='stars'):
    params['q'] = f'language:{language} is:public'
    params['sort'] = sort_by

    response = requests.get('https://api.github.com/search/repositories', params=params)

    if response.status_code == 200:
        data = response.json()
        repositories = data.get('items', [])            
        result = []
        for repo in repositories:
            language = repo.get('language', 'Unknown')
            result.append({
                'name': repo.get('name', 'Unknown'),
                'language': language
            })
        
        return result
    else:
        print(f'Error {response.status_code}')
        return []


def get_top_repositories(sort_by='stars'):
    params['sort'] = sort_by  # Устанавливаем метод сортировки
    response = requests.get('https://api.github.com/search/repositories', params=params)

    # Проверка успешности запроса
    if response.status_code == 200:
        data = response.json()  # Преобразование ответа в формат JSON
        repositories = data['items']  # Получение списка репозиториев из ответа
        return repositories
    else:
        print(f'Error {response.status_code}')  # Вывод ошибки, если запрос не успешен
        return None


def get_top_repositories(owner=None, sort_by='stars'):
    query = 'is:public'
    if owner:
        query += f' user:{owner}'

    params['q'] = query
    params['sort'] = sort_by
    
    response = requests.get('https://api.github.com/search/repositories', params=params)

    if response.status_code == 200:
        data = response.json()
        repositories = data['items']
        return repositories
    else:
        print(f'Error {response.status_code}')
        return None




def get_top_repositories(owner=None, sort_by='stars'):
    query = 'is:public'
    if owner:
        query += f' user:{owner}'

    params['q'] = query
    params['sort'] = sort_by
    
    response = requests.get('https://api.github.com/search/repositories', params=params)

    if response.status_code == 200:
        data = response.json()
        repositories = data['items']
        return repositories
    else:
        print(f'Error {response.status_code}')
        return None

# repositories = get_top_repositories(sort_by='stars')
# if repositories:
#     for index, repo in enumerate(repositories, start=1):
#         print(f'{index}. {repo["name"]} - {repo["stargazers_count"]} stars')











def top_test_language(language, sort_by='stars'):
    params_language = params.copy()  # Создаем копию params
    params_language['q'] = f'language:{language} is:public'
    params_language['sort'] = sort_by
    
    return make_github_request(params_language)



# def top_test_language(language, sort_by='stars'):
#     params = {
#         'q': f'language:{language} is:public',
#         'order': 'desc',
#         'per_page': 10
#     }
#     params['sort'] = sort_by
    
#     return make_github_request(params)



# repositories = top_test_language('python')
# if repositories:
#     for index, repo in enumerate(repositories, start=1):
#         print(f'{index}. {repo["name"]} - {repo["language"]}')



def top_test_repo(owner=None, sort_by='stars'):
    params = {
        'q': 'is:public',
        'order': 'desc',
        'per_page': 10
    }

    query = 'is:public'
    if owner:
        query += f' user:{owner}'

    params['q'] = query
    params['sort'] = sort_by
    
    return make_github_request(params)


# repositories = get_top_repositories(sort_by='stars')
# if repositories:
#     for index, repo in enumerate(repositories, start=1):
#         print(f'{index}. {repo["name"]} - {repo["stargazers_count"]} stars')




def top_test(owner=None, sort_by='stars'):
    query = 'is:public'
    if owner:
        query += f' user:{owner}'

    params['q'] = query
    params['sort'] = sort_by
    
    return make_github_request(params)

# repositories = top_test(sort_by='stars')
# if repositories:
#     for index, repo in enumerate(repositories, start=1):
#         print(f'{index}. {repo["name"]} - {repo["stargazers_count"]} stars')




"""
def get_commit_activity(owner, repo, since, until):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    prs = {'since': since, 'until': until}
    response = requests.get(url, params=prs)

    if response.status_code == 200:
        commits = response.json()
        commit_activity = {}
        for commit in commits:
            commit_date = commit['commit']['author']['date'][:10]  # extracting only date part
            commit_activity[commit_date] = commit_activity.get(commit_date, 0) + 1
        return commit_activity
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None


owner = 'Jorupbek'
repo = 'sewing-factory-back'
since = '2024-01-01T00:00:00Z'  # Начальная дата и время в формате ISO 8601
until = '2024-03-01T00:00:00Z'  # Конечная дата и время в формате ISO 8601

commit_activity = get_commit_activity(owner, repo, since, until)
if commit_activity:
    print(commit_activity)
    """

'''

def get_commit_activity(owner, repo, since, until):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'since': since, 'until': until}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        commit_activity = {}
        for commit in commits:
            commit_date = commit['commit']['author']['date'][:10]  # Извлечение только даты
            commit_activity[commit_date] = commit_activity.get(commit_date, 0) + 1
        return commit_activity
    else:
        print(f"Не удалось получить данные: {response.status_code}")
        return None
    
def count_total_commits(commit_activity):
    total_commits = sum(commit_activity.values())
    return total_commits

# Замените owner и repo на владельца и название репозитория
owner = 'Kylych-dev'
repo = 'reviro_test'
since = '2024-02-01T00:00:00Z'  # Начальная дата и время в формате ISO 8601
until = '2024-03-01T00:00:00Z'  # Конечная дата и время в формате ISO 8601


# Получение данных о коммитах
commit_activity = get_commit_activity(owner, repo, since, until)
if commit_activity:
    print("Количество коммитов на каждый день:")
    print(commit_activity)
    total_commits = count_total_commits(commit_activity)
    print(f"Общее количество коммитов за выбранный период времени: {total_commits}")


'''



def get_commit_activity(owner, repo, since, until):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'since': since, 'until': until}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        commit_activity = {}
        total_commits = 0
        for commit in commits:
            commit_date = commit['commit']['author']['date'][:10]  # Извлечение только даты
            commit_activity[commit_date] = commit_activity.get(commit_date, 0) + 1
            total_commits += 1
        return commit_activity, total_commits
    else:
        print(f"Не удалось получить данные: {response.status_code}")
        return None, None

# Параметры запроса
owner = 'Kylych-dev'
repo = 'reviro_test'
since = '2024-02-01T00:00:00Z'  # Начальная дата и время в формате ISO 8601
until = '2024-03-01T00:00:00Z'  # Конечная дата и время в формате ISO 8601

# Получение данных о коммитах
commit_activity, total_commits = get_commit_activity(owner, repo, since, until)
if commit_activity is not None and total_commits is not None:
    print("Количество коммитов на каждый день:")
    print(commit_activity)
    print(f"Общее количество коммитов за выбранный период времени: {total_commits}")