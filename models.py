from django.contrib.contenttypes import generic
from django.contrib.auth.models import User, Group
from django.db import models
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Ownable
from hs_core.models import AbstractResource

#
# To create a new resource, use these three super-classes. 
#

class SwatShareResource(Page, RichText):
    swat_model = models.FileField(
	upload_to = 'swatshareresource',
	help_text = 'this should be a swat model file',
    )
    swat_model_description = models.TextField(null=False, blank=True, default='', help_text = 'this should describe the model file')
    swat_model_count = models.IntegerField(null=False, default = 1, help_text = 'the count of the swat models')
    class Meta:
	verbose_name = 'Swatshare resource'
	
	

