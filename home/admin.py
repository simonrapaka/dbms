from django.contrib import admin
from .models import Patient
from .models import Disease
from .models import MedicalFacilities
from .models import MedicalRecord
from .models import Medicine
from .models import Prescription
from .models import HealthcareProviders

# Register your models here.
admin.site.register(Patient)
admin.site.register(Disease)
admin.site.register(MedicalFacilities)
admin.site.register(MedicalRecord)
admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(HealthcareProviders)