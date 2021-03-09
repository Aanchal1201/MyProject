from django.contrib import admin
from . models import Language,Title,Quiz,UserScore,Feedback
# Register your models here.

admin.site.register(Language)
admin.site.register(Title)
admin.site.register(Quiz)
admin.site.register(UserScore)
admin.site.register(Feedback)