from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book

def ajax(request):
    return render(request, "ajax.html")

# Create your views here.

@api_view(['GET'])
#client의 요청은 대부분 request라고 작성
def helloAPI(request):
    return Response("HEllO REST API")

from .serializers import BookSerializer
from rest_framework import status

@api_view(['POST', 'GET'])
def booksAPI(request, staus=None):
    #전송 방식을 확인하는 방법은 request.merhod를 확인하면 됨
    #print("1") #이 코드가 실행이 안되면 URL과 method 연결 실수
    #클라이언트가 전송한 데이터를 삽입
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status =status.HTTP_200_OK)

    elif request.method == 'POST':

        #클라이언트가 전송한 데이터를 Model이 사용할 수 있는 데이터로 전환
        serializer = BookSerializer(data=request.data)

        #print("2")#이 코드가 찍히지 않으면 Serializable 실패

        #유효성 검사
        if serializer.is_valid():
            #print("3")#이름이 잘못된 것
            serializer.save() #데이터 저장
            #성공했을 때 전송한 데이터를 다시 전송
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #실패했을 때 처리
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#기본키를 가지고 데이터를 1개 찾아오는데 없으면 404에러 발생
from rest_framework.generics import get_object_or_404

@api_view(['GET'])
def bookAPI(request, bid):
    #기본키를 가지고 데이터 1개 가져오기
    book = get_object_or_404(Book, bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status.HTTP_200_OK)
