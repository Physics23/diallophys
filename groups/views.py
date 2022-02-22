from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models
#from django.core.urlsresolvers import reverse
from django.urls import reverse
from django.views import generic
from groups.models import Group,GroupsMember
from . import models
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib import messages



class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields=('name', 'description')
    model = Group


class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model=Group

class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self,*args, **kwargs):
        return reverse('groups:single', kwargs= {'slug':self.kwargs.get('slug')})

    def get(self,request, *args, **kwargs):
        group = get_object_or_404(Group, slug= self.kwargs.get('slug'))
        try:
            GroupsMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Already a member!')
        else:
            messages.success(self.request, 'You are now a member!')
        return super().get(request ,*args, **kwargs)




class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self,*args, **kwargs):
       return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, *args, **kwargs):
        try:
            memberships= models.GroupsMember.objects.filter(
            user=self.request.user, group__slug=self.kwargs.get('slug')
            ).get()
        except models.GroupsMember.DoesNotExist:
            messages.warning(self.request, 'Sorry you are not in this group!')
        else:
            memberships.delete()
            messages.success(self.request, 'You have left the group')
        return super().get(self.request, *args, **kwargs)
