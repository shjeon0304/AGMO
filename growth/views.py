from django.shortcuts import render,redirect

from .models import Crop,Task

def growth(request):
    crops = Crop.objects.all()
    return render(request, 'growth/index.html', {'crops': crops})

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