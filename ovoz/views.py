import io
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View
from users.models import User, Davomat
from users.forms import LoginForm
from .forms import ElomForm, DavomatForm
from .models import Elon, Statistika





def pie_chart(request, pk):
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
            elonlar = Elon.objects.all()
            elonlar_soni = elonlar.__len__
            aktivlar = Elon.objects.filter(yoqish=False)
            aktivlar_soni = aktivlar.__len__
            baholangan = Elon.objects.filter(yoqish=True)
            baholangan_soni = baholangan.__len__

           
        except:
            azo_soni = 'o'
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
            data = Elon.objects.filter(baza='0')
        except:
            data = ''

        context = {
            'data':data,
        }
        return render(request, 'ovoz/taklif.html', context)
    
    def post(self, request):
        
        
        context = {

        }
        return render(request, 'asosiy/home.html', context)
    
    

class ElonView(View):
    def get(self, request):
        form = ElomForm()

        context = {
            'form':form,
        }
        return render(request, 'ovoz/elon.html', context)
    
    def post(self, request):
        form = ElomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


        context = {
            'form':form,
        }
        return render(request, 'ovoz/elon.html', context)
    
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
    
class YoqishView(View):
    def get(self, request, pk):
        try:
            data = Elon.objects.get(id=pk)
            data.yoqish = 'True'
            data.baza = '1'
            data.save()
            return redirect('/taklif/')
        
        except:
            return HttpResponse('<h1>Taklif yoqilmadi!!!</h1>')
        
class TakliflarAzoView(View):
    def get(self, request):
        try:
            data = Elon.objects.filter(baza='1')
        except:
            data = ''

        context = {
            'data':data,
        }
        return render(request, 'ovoz/taklif_azo.html', context)
        

class RozilarView(View):
    def get(self, request, pk):


        context = {

        }
        return render(request, 'ovoz/rozilar.html', context)
    
class QarshilarView(View):
    def get(self, request, pk):


        context = {

        }
        return render(request, 'ovoz/qarshilar.html', context)
    
class BetaraflarView(View):
    def get(self, request, pk):


        context = {

        }
        return render(request, 'ovoz/betaraflar.html', context)
    
class DavomatView(View):
    def get(self, request):
        try:            
            bugun = date.today()
            print(bugun)
            davomat = Davomat.objects.all()
            for d in davomat:
                sana = f'{d.sana}'
                print(sana[:10])
            data = User.objects.filter(lavozim='azo')
            for u in data:
                print(u.id)
                davomat = Davomat.objects.filter(id=u.id)
                print(davomat)
        except:            
            data = ''
            davomat = ''
        context = {
            'data':data,
            'davomat':davomat,
        }
        return render(request, 'ovoz/davomat.html', context)
    
    def post(self, request):
        form = DavomatForm(request.POST)        
        try:
            if form.is_valid():
                new = form.cleaned_data
                new.user = '1'
                new.save()
                return redirect('/davomat/')
            else:
                return HttpResponse('Bajarildi {user}')
        except:
            form = DavomatForm()


        context = {
            'form':form,
        }
        return render(request, 'ovoz/elon.html', context)
    
def davomatlar(request, pk):
    user = User.objects.get(id=pk)
    try:
        data = Davomat.objects.filter(id=pk)
        if data is not None :
            Davomat.objects.update(user=user.id, bor='bor')
            return HttpResponse('Bajarildi {update}')
        else:
            Davomat.objects.create(user=user.id, bor='bor')
            return HttpResponse('Bajarildi {create}')
        
        
            
    except:
        return redirect('/davomat/')


    