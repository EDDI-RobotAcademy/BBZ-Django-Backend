from django.shortcuts import render
from rest_framework import viewsets

from board.entity.models import Board
from board.service.board_service_impl import BoardServiceImpl


# Create your views here.
class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all()
    boardService = BoardServiceImpl.getInstance()
