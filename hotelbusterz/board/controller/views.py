from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from board.serializers import BoardSerializer
from board.entity.models import Board
from board.service.board_service_impl import BoardServiceImpl


# Create your views here.
class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all()
    boardService = BoardServiceImpl.getInstance()

    def list(self, request):
        boardList = self.boardService.list()
        serializer = BoardSerializer(boardList, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BoardSerializer(data=request.data)

        if serializer.is_valid():
            board = self.boardService.createBoard(serializer.validated_data)
            return Response(BoardSerializer(board).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        board = self.boardService.readBoard(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def modify(self, request, pk=None):
        board = self.boardService.readBoard(pk)
        serializer = BoardSerializer(board, data=request.data, partial=True)

        if serializer.is_valid():
            board = self.boardService.modifyBoard(serializer.validated_data, pk)
            return Response(BoardSerializer(board).data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def removeBoard(self, request, pk=None):
        self.boardService.removeBoard(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

