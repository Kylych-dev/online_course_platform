from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from .services import add_reaction, remove_reaction, get_fans
from .serializers import ArticleSerializer

class ReactionMixin:
    """
    Миксин для добавления реакций к ViewSet
    Требует наличие модели Article в ViewSet
    """

    @action(detail=True, methods=['post'])
    def like(self, request: Request, pk: int | str = None) -> Response:
        """
        Добавляет лайк к тексту

        :param request: Request
        :param pk: id article
        :return: Response с статусом операции
        """
        article = self.get_object()
        add_reaction(article, request.user, is_like=True)
        return Response(
            {'status': 'success'},
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['post'])
    def dislike(self, request: Request, pk: int | str = None) -> Response:
        """
        Добавляет дизлайк к тексту

        :param request: Request
        :param pk: id article
        :return: Response с статусом операции
        """
        article = self.get_object()
        add_reaction(article, request.user, is_like=False)
        return Response(
            {'status': 'success'},
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['delete'])
    def unlike(self, request: Request, pk: int | str = None) -> Response:
        """
        Удаляет реакцию с текста

        :param request: Request
        :param pk: id article
        :return: Response с статусом операции
        """
        article = self.get_object()
        removed = remove_reaction(article, request.user)
        if not removed:
            return Response(
                {'error': 'Reaction not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

    @action(detail=True, methods=['get'])
    def fans(self, request: Request, pk: int | str = None) -> Response:
        """
        Возвращает список пользователей, поставивших реакции

        :param request: Request
        :param pk: id article
        :return: Response со списком пользователей
        """

        article = self.get_object()
        fans = get_fans(article)
        serializer = ArticleSerializer(fans, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


















