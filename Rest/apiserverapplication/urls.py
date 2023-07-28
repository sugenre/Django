from django.urls import path
from .views import helloAPI
from .views import booksAPI, bookAPI

urlpatterns =[
    #/example/hello/ 요청이 오면 helloAPI 함수가 처리
    #apiserverproject에서 example/을 만들어서
    # 총 경로가 /example/hello/ 이게 됨
    path("hello/", helloAPI),
    #/example/fbv/books  요청이 오면 boolAPI 함수가 처리
    path("fbv/books", booksAPI),

    #bid를 방아서 1개의 데이터를 찾아오는 것을 bookAPI 함수가 처리
    path("fbv/book/<int:bid>/", bookAPI)
]