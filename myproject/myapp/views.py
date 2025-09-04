from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def second_page(request): # ฟังก์ชันใหม่
    return render(request, 'myapp/second_page.html', {'message': 'คุณมาถึงหน้าสองแล้ว!'})