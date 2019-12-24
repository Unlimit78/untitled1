from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.signing import BadSignature
from django.contrib.auth import logout
from django.contrib import messages
from .models import AdvUser,Photos
from .forms import ChangeUsersInfo,RegisterUserForm,PhotoForm

from friends.models import Friend


def index(request):
    admin = AdvUser.objects.get(is_superuser=True)
    context = {'admin':admin}
    return render(request,'main/index.html',context)

class UserLogin(LoginView):
    template_name = 'main/login.html'

class UserLogout(LoginRequiredMixin,LogoutView):
    template_name = 'main/logout.html'

class ChangeInfo(SuccessMessageMixin,LoginRequiredMixin,UpdateView,):
    model = AdvUser
    template_name = 'main/change_info.html'
    form_class = ChangeUsersInfo
    success_url = reverse_lazy('profile')
    success_message = 'Info has been changed ...'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request,*args,**kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset,pk=self.user_id)

class ChangePassword(SuccessMessageMixin,LoginRequiredMixin,PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('profile')
    success_message = 'Password has been changed ...'

class RegisterUserView(CreateView):
    model=AdvUser
    template_name = 'main/register_user.html'
    form_class=RegisterUserForm
    success_url = reverse_lazy('register_done')

class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'

class DeleteUser(LoginRequiredMixin,DeleteView):
    model=AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('index')
    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        del_friends = Friend.objects.filter(from_user=request.user)
        del_friends.delete()
        return super().dispatch(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        logout(request)
        messages.add_message(request,messages.SUCCESS,'User deleted...')
        return super().post(request,*args,**kwargs)
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset,pk=self.user_id)

@login_required
def profile(request):
    photos = Photos.objects.filter(location=request.user)
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = Photos.objects.create(location=request.user,photo=form.cleaned_data['photos'])
            return redirect('profile')
    return render(request, 'main/profile.html', {'form': form, 'photos': photos})

def page(request):
    return render(request, 'main/templates/layout/myfile.html')
