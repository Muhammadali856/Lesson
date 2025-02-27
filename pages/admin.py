from django.contrib import admin
from pages.models import ContactModel

admin.site.register(ContactModel) # This is the correct way to register the model in the admin panel.
