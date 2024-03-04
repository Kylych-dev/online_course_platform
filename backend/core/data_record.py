import psycopg2
from utils import get_github_repositories


def insert_repository(repo_data):
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cur = conn.cursor()

    sql_query = "INSERT INTO repositories (repo, owner, position_cur, position_prev, stars, watchers, forks, open_issues, language) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(sql_query, repo_data)
    
    conn.commit()
    cur.close()
    conn.close()




def parse_and_save_repositories():
    params = {
        'q': 'is:public',
        'order': 'desc',
        'per_page': 100
    }
    repositories = get_github_repositories(params)
    for repo in repositories:
        repo_data = (
            repo['full_name'],
            repo['owner']['login'],
            repo['stargazers_count'],
            repo['watchers_count'],
            repo['forks_count'],
            repo['open_issues_count'],
            repo['language']
        )
        insert_repository(repo_data)