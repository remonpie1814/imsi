from django.shortcuts import render
from .models import Coffee
from .forms import CoffeeForm
# Create your views here.
def index(request):
    return render(request,"index.html",{})

def coffee_view(request):
    # Coffee모델에 담긴 모든 객체를 coffee_all에 담는다
    coffee_all=Coffee.objects.all()
    # 만약에 request가 POST면? #POST를 바탕으로 Form을 완성하고 Form이 유효하면 저장한다
    if request.method=="POST":
        # POST의 내용을 바탕으로 form을 만든다
        form=CoffeeForm(request.POST)
        # 양식이 유효하면 .save()를 실행한다.
        if form.is_valid():
            form.save()


    form=CoffeeForm()
    
    return render(request,"coffee.html",{"coffee_list":coffee_all,"coffee_form":form})