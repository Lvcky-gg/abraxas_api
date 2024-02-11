from django.contrib import admin
from .models.person import Person
from .models.publication import Publication
from .models.quote import Quote
from .models.verification import Verification
from .models.region import Region

admin.site.register(Person)
admin.site.register(Publication)
admin.site.register(Quote)
admin.site.register(Verification)
admin.site.register(Region)

# Register your models here.
