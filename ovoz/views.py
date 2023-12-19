import io
import time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, get_user_model
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View
from users.models import User, Davomat
from users.forms import LoginForm
from .forms import TaklifForm, DavomatForm
from .models import Taklif, Statistika, Baxo



@csrf_exempt
def diyogramma(request, pk):
    data = Statistika.objects.filter(id=pk)
    for d in data:
        rozi = int(d.rozilar)
        qarshi = int(d.qarshilar)   
    
        labels = ['rozilar', 'qarshilar', 'betaraf', 'qatnashmadi']
        sizes = [rozi, qarshi, 5, 10]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        response = HttpResponse(buf.read(), content_type='image/png')
        response['Content-Disposition'] = 'inline; filename=diagram.png'   
        return response


@csrf_exempt   
def kirish(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                user.save()
                return redirect('/')
            
        return render(request, 'asosiy/kirish.html')
    except:                
        return redirect('/kirish')
    
@csrf_exempt  
def home(request):
    try:
            azolar = User.objects.filter(lavozim='azo')
            azo_soni = azolar.__len__
            elonlar = Taklif.objects.all()
            elonlar_soni = elonlar.__len__
            aktivlar = Taklif.objects.filter(yoqish=False)
            aktivlar_soni = aktivlar.__len__
            baholangan = Taklif.objects.filter(yoqish=True)
            baholangan_soni = baholangan.__len__         
            
           
    except:
            azo_soni = '0'
            elonlar_soni = '0'
            aktivlar_soni = '0'
            baholangan_soni = '0'


    context = {
            'azo_soni':azo_soni,
            'elonlar_soni':elonlar_soni,
            'aktivlar_soni':aktivlar_soni,
            'baholangan_soni':baholangan_soni,
        }
    return render(request, 'asosiy/home.html', context)
        

    
    
@csrf_exempt
def azo_qoshish(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            last_name = request.POST['last_name']
            first_name = request.POST['first_name']
            lavozim = request.POST['lavozim']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if User.objects.filter(username=username):
                return HttpResponse("Bunday azo mavjud") 
            elif password1 != password2:
                return HttpResponse("Parollar bir biriga teng emas")
            else:
                user = get_user_model().objects.create(
                    username = username, last_name = last_name, 
                    first_name = first_name, lavozim=lavozim, 
                    password = make_password(password1)) 
                user.is_active = False
                user.is_staff = False
                
                return redirect('/azo/')
        return render(request, 'users/azo_qoshish.html')
    except:
        return HttpResponse('Azo qo`shilmadi')


@csrf_exempt
def statistika(request):
    try:
        baxo = Baxo.objects.all()
        if baxo:
            for b in baxo:
                static = Statistika.objects.filter(taklif_id=b.taklif_id)
                if static:
                    Statistika.objects.filter(taklif_id =b.taklif_id).update(                            
                            rozilar="0",
                            qarshilar = "0",
                            betaraflar = "0",
                            qatnashmaganlar = "0"
                        )                        
                    return render(request, 'ovoz/statistika.html')
                else:                   
                    data = Statistika.objects.create(
                        taklif_id =b.taklif_id,
                        rozilar="0",
                        qarshilar = "0",
                        betaraflar = "0",
                        qatnashmaganlar = "0"
                    )
                    data.save()
                    return render(request, 'ovoz/statistika.html')
                
    except:
        return render(request, 'xato/404.html')     

       
      
    return render(request, 'ovoz/statistika.html')


@csrf_exempt
def taklif(request):
    try:
        kiritilgan = Taklif.objects.filter(yoqish=False)
        baholangan = Taklif.objects.filter(yoqish=True).filter(tugash=False)
                
                
    except:
        kiritilgan = ''
        baholangan = ''

    context = {
        'kiritilgan':kiritilgan,
        'baholangan':baholangan,
    }
    return render(request, 'ovoz/taklif.html', context)


@csrf_exempt
def taklif_kiritish(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            nomzod = request.POST['nomzod']
            vaqt = request.POST['vaqt']
            data = Taklif.objects.create(name=name, nomzod=nomzod, vaqt=vaqt)
            data.save()
            return redirect('/taklif/')                
            
        return render(request, 'ovoz/taklif_kiritish.html')
    except:                
        return render(request, 'ovoz/404.html')
    

@csrf_exempt   
def azolar(request):
    try:
        data = User.objects.filter(lavozim='azo')
    except:
        data = ''

    context = {
        'data':data,
    }
    return render(request, 'ovoz/azolar.html', context)

    

@csrf_exempt
def taklif_yoqish(request, pk):
    try:
        bugun = datetime.now()
        data = Taklif.objects.get(id=pk)
        vaqt = bugun + timedelta(minutes=data.vaqt)
        boshlanish_vaqti = f'{bugun}'
        tugash_vaqti = f'{vaqt}'
        data.boshlanish_vaqti = boshlanish_vaqti
        data.tugash_vaqti = tugash_vaqti
        data.yoqish = True        
        data.save()
         

        return redirect('/taklif/')
        
    except:
        return render(request, "xato/404.html")



@csrf_exempt
def taklif_ochirish(request, pk):
    try:
        data = Taklif.objects.get(id=pk)
        data.boshlanish_vaqti = ''
        data.tugash_vaqti = ''
        data.yoqish = False
        data.save()
        return redirect('/taklif/')
        
    except:
        return render(request, "xato/404.html")

    

def taklif_azo(request):
    try:
        bugun = datetime.today()
        data = Taklif.objects.filter(yoqish=True).filter(tugash=False)
        for d in data:
            tugash = f'{d.tugash_vaqti}'
            sana = f'{bugun}'
            if tugash[:16] <= sana[:16]:
                taklif = Taklif.objects.get(id=d.id)
                taklif.tugash = True
                taklif.save()
                print('bajarildi')
            else:
                print('bajarilmadi')
                
    except:
        data = ''            

    context = {
        'data':data,
    }
    return render(request, 'ovoz/taklif_azo.html', context)


 


@csrf_exempt
def roziman(request, pk):
    try:
        taklif = Taklif.objects.filter(yoqish=True).filter(tugash=True)
        if taklif:
            for t in taklif:
                baxo = Baxo.objects.filter(taklif_id=t.id).filter(user_id=request.user.id)
                if baxo:
                    return render(request, 'xato/ovoz.html')
                else:
                    data = Baxo.objects.create(
                        user_id = request.user.id ,
                        taklif_id = t.id,
                        baxo = "roziman"
                    )
                    data.save()
                    
                    return render(request, 'xato/200.html')   


    except:
        return render(request, 'xato/404.html')


@csrf_exempt
def qarshiman(request, pk):
    try:
        taklif = Taklif.objects.filter(yoqish=True).filter(tugash=True)
        if taklif:
            for t in taklif:
                baxo = Baxo.objects.filter(taklif_id=t.id).filter(user_id=request.user.id)
                if baxo:
                    return render(request, 'xato/ovoz.html')
                else:
                    data = Baxo.objects.create(
                        user_id = request.user.id ,
                        taklif_id = t.id,
                        baxo = "qarshiman"
                    )
                    data.save()
                    
                    return render(request, 'xato/200.html')   


    except:
        return render(request, 'xato/404.html')
    



@csrf_exempt
def betarafman(request, pk):
    try:
        taklif = Taklif.objects.filter(yoqish=True).filter(tugash=True)
        if taklif:
            for t in taklif:
                baxo = Baxo.objects.filter(taklif_id=t.id).filter(user_id=request.user.id)
                if baxo:
                    return render(request, 'xato/ovoz.html')
                else:
                    data = Baxo.objects.create(
                        user_id = request.user.id ,
                        taklif_id = t.id,
                        baxo = "betarafman"
                    )
                    data.save()
                    
                    return render(request, 'xato/200.html')   


    except:
        return render(request, 'xato/404.html')



@csrf_exempt 
def davomat(request):
    try:   
        borlar = Davomat.objects.filter(aktiv=True)
        yoqlar = Davomat.objects.filter(aktiv=False)            
            
    except:            
        borlar = ''
        yoqlar = ''
    context = {
            'borlar':borlar,
            'yoqlar':yoqlar,
    }
    return render(request, 'ovoz/davomat.html', context)  


    
    
@csrf_exempt   
def bor(request, pk):
    try:       
        Davomat.objects.filter(id=pk).update(aktiv=True)         
        return redirect('/davomat/')
    
    except:
        return render(request, "xato/404.html")   
    

@csrf_exempt
def yoq(request, pk):
    try:       
        Davomat.objects.filter(id=pk).update(aktiv=False)        
        return redirect('/davomat/')                  
  
    except:
        return render(request, "xato/404.html")


    
@csrf_exempt
def davomat_yangilash(request):
    try:
        user = User.objects.filter(lavozim='azo')
        if user:
            for u in user:
                davomat = Davomat.objects.filter(user_id=u.id)
                if davomat: 
                    print('update')
                    Davomat.objects.filter(user_id=u.id).update(
                        sana=datetime.today(), 
                        aktiv=False
                    )  
                        
                else:
                    data = Davomat.objects.create(
                        user_id = u.id,
                        familya = u.last_name,
                        ism = u.first_name,
                        aktiv = False,
                        sana = datetime.today()
                    )
                    data.save()
                    print('create')

        return redirect("/davomat/")           



    except:
        return render(request, "xato/404.html")
    

    

    
    