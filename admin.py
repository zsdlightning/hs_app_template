from mezzanine.pages.admin import PageAdmin
from django.contrib.gis import admin
from .models import SwatShareResource

admin.site.register(SwatShareResource, PageAdmin)
