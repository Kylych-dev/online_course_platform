from apps.articles.models import Like, Article
from apps.users.models import CustomUser


def add_reaction(
        article: Article,
        user: CustomUser,
        is_like: bool = True
) -> Like:
    """
    Добавляет реакцию пользователя на текст

    :param article: объекта текста
    :param user: авторизованный пользователь
    :param is_like: тип реакции (True/False лайк/дизлайк)
    :return: созданный объект Like
    """
    like, created = Like.objects.update_or_create(
        article=article,
        user=user,
        defaults={'is_like': is_like}
    )
    return like

def remove_reaction(        # ToDo: в оболочке проверит удаление лайка
        article: Article,
        user: CustomUser,
) -> bool:
    """
    Удаляет реакцию пользователя на текст

    :param article: объекта текста
    :param user: авторизованный пользователь
    :return: True/False удалена/не найдена
    """
    deleted, _ = Like.objects.filter(
        article=article,
        user=user
    ).delete()
    return deleted > 0

def get_fans(article: Article) -> list:
    """
    Возвращает список пользователей, поставивших реакции на текст

    :param article: объекта текста
    :return: QuerySet пользователей
    """
    return CustomUser.objects.filter(likes__in=[article])

