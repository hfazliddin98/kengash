import io
import time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View
from users.models import User, Davomat
from users.forms import LoginForm
from .forms import TaklifForm, DavomatForm
from .models import Taklif, Statistika, Baxo
from .vaqt import tugatish






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


class HomeView(View):
    def get(self, request):
        form = LoginForm()
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
            'form':form,
            'azo_soni':azo_soni,
            'elonlar_soni':elonlar_soni,
            'aktivlar_soni':aktivlar_soni,
            'baholangan_soni':baholangan_soni,
        }
        return render(request, 'asosiy/home.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('Foydalanuvchi yoki parol xato !!!')
        
        context = {
            'form':form,
        }
        return render(request, 'asosiy/home.html', context)
    

class StatistikaView(View):
    def get(self, request):
        try:
            data = Statistika.objects.all()
            x = [x.rozilar for x in data]
            y = [y.qarshilar for y in data]
            print(f'{x} va {y}')

        except:
            return render(request, 'xato/404.html')
        

       
        context = {
            'data':data,
        }
        return render(request, 'ovoz/statistika.html', context)
    

class TaklifView(View):
    def get(self, request):
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
    
    def post(self, request):
        
        
        context = {

        }
        return render(request, 'asosiy/home.html', context)
    
    

class TaklifKiritishView(View):
    def get(self, request):
        form = TaklifForm()

        context = {
            'form':form,
        }
        return render(request, 'ovoz/taklif_kiritish.html', context)
    
    def post(self, request):
        form = TaklifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/taklif/')


        context = {
            'form':form,
        }
        return render(request, 'ovoz/taklif_kiritish.html', context)
    
class AzoView(View):
    def get(self, request):
        try:
            data = User.objects.filter(lavozim='azo')
        except:
            data = ''

        context = {
            'data':data,
        }
        return render(request, 'ovoz/azolar.html', context)
    
    
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

    

        
class TakliflarAzoView(View):
    def get(self, request):
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
            print('except')

        context = {
            'data':data,
        }
        return render(request, 'ovoz/taklif_azo.html', context)
        

class RozilarView(View):
    def get(self, request, pk):
        try:
            data = Baxo.objects.get(taklif_id=pk)
            if data:
                # Baxo.objects.filter(user_id=request.user.id).update(baxo='roziman')
                return HttpResponse("Update")
            else:
                # Baxo.objects.create(
                #     taklif_id=pk,
                #     user_id=request.user.id,
                #     baxo='roziman'
                # )
            # return redirect("/taklif_azo/")
                return HttpResponse('Create')



        except:            
            return HttpResponse('Bajarilmadi')

            # return redirect("/taklif_azo/")
        
    
class QarshilarView(View):
    def get(self, request, pk):


        return redirect("/taklif_azo/")

    
class BetaraflarView(View):
    def get(self, request, pk):


        return redirect("/taklif_azo/")
    

class DavomatView(View):
    def get(self, request):
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
    
    
    
def bor(request, pk):
    try:       
        Davomat.objects.filter(id=pk).update(aktiv=True)         
        return redirect('/davomat/')
    
    except:
        return render(request, "xato/404.html")   
    


def yoq(request, pk):
    try:       
        Davomat.objects.filter(id=pk).update(aktiv=False)        
        return redirect('/davomat/')                  
  
    except:
        return render(request, "xato/404.html")


    

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
    

    

    
    