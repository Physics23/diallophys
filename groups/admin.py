
from django.db import models
from groups.models import GroupsMember

from django.contrib import admin
from . import models

# Register your models here.
class GroupMemberInline(admin.TabularInline):
    model = models.GroupsMember

admin.site.register(models.Group)
