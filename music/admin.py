# # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Gform, Question

admin.site.register(Gform)
admin.site.register(Question)

