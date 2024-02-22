from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog


# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def home(request):
    blogs = Blog.objects.order_by('-id')
    return render(request, 'home.html',{'blogs':blogs})

def new(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'new.html', {'fulltext':full_text,'wordlist':len(word_list),'dictionary': word_dictionary.items()})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})

def create(request):
    return render(request, 'create.html')

def postcreate(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/homeapp/detail/'+str(blog.id))

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/homeapp/detail/' + str(blog.id))

    else:
        return render(request, 'update.html')

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

#일지 기록
from .models import Cropdata

def diary(request):
    pages = Cropdata.objects.all()
    context = {"pages": pages}
    return render(request, 'diary.html', context)

def page_create(request):
    if request.method =="POST":
        form = PageForm(request.POST)
        if form.is_valid():
            new_page = form.save()
            return redirect("page-detail", page_id=new_page.id)
    else:
        form = PageForm()
    return render(request, "diarys/page_form.html", {"form": form})


def write(request):
    posts = Cropdata()
    posts.crop = request.POST['crop']
    posts.fieldNum = request.POST['num']
    posts.cropWork = request.POST['cropwork']
    posts.content = request.POST['content']
    posts.pesticide = request.POST['pesticide']
    posts.save()
    return render(request, 'view_diary.html', {'posts':posts})



#calender
import calendar
import json
#import .models import Month, Day

def calender(request):
    yearCalender = calendar.HTMLCalendar().formatyear(2021)
    context = {
        'YC': yearCalender,
    }
    return render(request, 'calender.html', context)


#growth
from .models import Crop,Task

def growth(request):
    crops = Crop.objects.all()
    return render(request, 'growth.html', {'crops': crops})

def update_task_progress(request, pk): #다른거랑 연계해서 일정 업데이트 되면 진척도 바꾸는 거
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        new_progress = request.POST['progress']
        task.progress = new_progress
        task.save()

        return redirect('index')

    return render(request, 'update_task_progress.html', {'task': task})



def create_crop(request):
    if request.method == 'POST':
        name = request.POST['name']
        new_crop = Crop.objects.create(name=name)

        # Crop에 따라 정해진 Task 생성 뒤에 내용은 바꿀 수 있을듯 작물이랑 재배법 선택하면 이에 따라서 추가되는거 
        # 작물선택 > 이걸로 데이터베이스에 저장 > 일지 쓸 때랑 진척도 나타낼 때 사용하면 될 듯
        if name == '토마토':
            Task.objects.create(crop=new_crop, name='씨 뿌리기')
            Task.objects.create(crop=new_crop, name='물 주기')
            Task.objects.create(crop=new_crop, name='햇빛쬐기')
        elif name == '오이':
            Task.objects.create(crop=new_crop, name='씨 뿌리기')
            Task.objects.create(crop=new_crop, name='덩굴 잡기')
            Task.objects.create(crop=new_crop, name='물 주기')

        return redirect('index')

    return render(request, 'create_crop.html')
