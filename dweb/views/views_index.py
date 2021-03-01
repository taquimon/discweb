from django.shortcuts import render, HttpResponse
from ..connection import MysqlConnection

def index(request):
    mysql = MysqlConnection().query("select * from users")
    for u in mysql:
        print(u)
    return render(request, 'dweb/productos.html')
