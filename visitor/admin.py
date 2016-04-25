from django.contrib import admin
from visitor.models import Person
from visitor.models import Staff
from visitor.models import Visitor
from visitor.models import Comment
from visitor.models import Event


admin.site.register(Person)
admin.site.register(Staff)
admin.site.register(Visitor)
admin.site.register(Comment)
admin.site.register(Event)

# Register your models here.
