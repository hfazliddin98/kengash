from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import RoyhatForm


class RoyhatView(View):
    def get(self, request):
        form = RoyhatForm()

        context = {
            'form':form,
        }
        return render(request, 'users/royhat.html', context)
    
    def post(self, request):
        form = RoyhatForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()

            return redirect('/')

        context = {
            'form':new_user,
        }
        return render(request, 'users/royhat.html', context)