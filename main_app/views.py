from django.shortcuts import render, redirect
from django.views import View # <- View class to handle requests
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Destination, Spot, List

from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm #add this

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name= "about.html"


class SpotList(TemplateView):
    template_name = "spot_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["spots"] = Spot.objects.all()
        return context

class SpotCreate(View):
    def post(self, request, pk, **kwargs):
        name = request.POST.get('name')
        image = request.FILES.get('image')
        description =request.POST.get('description') 
        destination = Destination.objects.get(pk=pk)
        Spot.objects.create(name=name, image=image, description=description, destination=destination)
        return redirect('destination_detail', pk=pk)


class DestinationCreate(CreateView):
    model = Destination
    fields = ['name', 'image', 'description', 'verified_destination']
    template_name = "destination_create.html"
    success_url = '/destinations/'

class DestinationList(TemplateView):
    template_name = "destination_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.request.GET.get('name')
        if name != None:
            # This is essentially a regex matcher that's built in for us. It's searching for anything where the name of the Destination contains (at any point) this name if there is a query
            context["destinations"] = Destination.objects.filter(name__icontains=name)
        else:
            context["destinations"] = Destination.objects.all()
        return context

class DestinationDetail(DetailView):
    model = Destination
    template_name = "destination_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lists"] = List.objects.all()
        return context

class DestinationUpdate(UpdateView):
    model = Destination
    fields = ['name', 'image', 'description', 'verified_destination']
    template_name = "destination_update.html"
    success_url = '/destinations/'


class DestinationDelete(DeleteView):
    model = Destination
    template_name = "destination_delete.html"
    success_url = '/destinations/'

class ListAssoc(View):
    def get(self, request, pk, spot_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            List.objects.get(pk=pk).spots.remove(spot_pk)
        if assoc == "add":
            List.objects.get(pk=pk).spots.add(spot_pk)
        return redirect('home')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('home')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('home')
			else:
				messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('home')