from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.request import Request
from rest_framework.views import View
from typing import Any

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Any) -> bool:
        """
            Проверяет, является ли текущий пользователь владельцем объекта.

            Аргументы:
            - request: объект запроса (содержит данные о пользователе, методе и т. д.)
            - view: представление (может быть полезно, если нужна информация о действии)
            - obj: объект модели, к которому проверяется доступ (например, Article)

            Возвращает:
            - True, если метод запроса безопасный (GET, HEAD, OPTIONS)
            - Выбрасывает PermissionDenied, если пользователь не владелец
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.owner != request.user:
            raise PermissionDenied('Вы не являетесь владельцем этого текста.')

        return True
