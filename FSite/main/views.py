from django.shortcuts import render

def messange(request):
    data = {
        'value' : ['(Страна Россия, город Иваново)']
    }
    return render(request, 'main/messange.html', data)


def index(request):
    data = {
        'values' : ['В столбик', 'через запятую', 'просто']
    }
    return render(request, 'main/index.html', data)