from django.shortcuts import render
from one.models import Register
from django.views.generic import DetailView
from one import models
import json
from pprint import pprint

# Create your views here.
def register(request):
    if request.method == 'POST':
        reg=Register()
        reg.name=request.POST['name']
        reg.age=request.POST['age']
        reg.clas=request.POST['clas']
        reg.marks=request.POST['marks']
        reg.save()

        return render(request,'one/success.html')
    else:
        return render(request,'one/signup.html')

def start(request):
    return render(request,'one/signup.html')
def view(request):
    object=Register.objects.all()
    return render(request,'one/view.html',{'object':object})
class ViewDetailView(DetailView):
    model=models.Register
    context_object_name = 'details'
    template_name='one/detail.html'
def jso(request):
    '''data = [
        {
            "name": "satya",
            "age": 40,
            "class":"btech",
            "marks":100,
        },
         {
            "name": "satya1",
            "age": 41,
            "class":"btech1",
            "marks":100,
        }
    ]'''
    '''file = open("C:/Users/User/Desktop/back_end/ajir/one/json.json","r")
    data=file.read()
    json_string = json.dumps(data)
    datastore = json.loads(json_string)
    print(datastore[0])'''

    with open("C:/Users/User/Desktop/back_end/ajir/one/json.json") as f:
        data=json.load(f)
    for x in data['states']:
        print(x)









    #json_string = json.dumps(data)
    #datastore = json.loads(json_string)
    #print(data[0])
    #name=datastore['satya']['name']
    #age=datastore['satya']['age']
    #clas=datastore['satya']['class']
    #marks=datastore['satya']['marks']
    #Register.objects.create(name=name,age=age,clas=clas,marks=marks)

    #print(datastore)
    return render(request,'one/success.html')
