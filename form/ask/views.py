from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import InputForm
from .models import InputModel
import json

def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            name_input = form.cleaned_data['name0'] #проверка значения поля, name_input = текст в поле, cleaned_data - это результат вызова очищающих и валидирующих функций
            data = json.dumps(name_input,ensure_ascii=False) #сериализация obj в json-строку
            InputModel.objects.create(data=data,field='name0')

            for count in range(1,len(request.POST)-1): #request.POST словарь, и len показывает количество объектов
                query = 'name' + str(count)
                input_value = request.POST[query] #значение внутри поля, если больше 1го заполненного поля
                if input_value:
                    data = json.dumps(input_value,ensure_ascii=False)
                    field = json.dumps(query)
                    InputModel.objects.create(data=data,field=field)
                count += 1
        return redirect('/3/')
    else:
        form = InputForm()
    return render(request, 'index.html',{'form': form}) #{} - словарь значений для добавления в контекст шаблона
                    #request - объект запроса, использованный для генерации ответа
def done(request):
    query = InputModel.objects.all().values('id','field','data') #назначаем в переменную все объекты бд
    json_list = list(query)
    return render(request, 'done.html', {'json_list' : json_list})
