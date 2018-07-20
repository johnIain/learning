from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class my_middleware(MiddlewareMixin):
    def process_request(self,request):
        Method = request.method
        if Method == 'POST':
            username = request.COOKIES.get('cookie_username', '')
            print("IP:",request.get_host())
            print("URL:",request.get_host() + request.path)
            print('username',username)
