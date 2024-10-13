from django.test import TestCase

# Create your tests here.
from django.core.exceptions import ObjectDoesNotExist
from microgrids.models import Img

try:
    # Try to get the Img object
    img = Img.objects.get(name_h='Big_Microgrid')
except ObjectDoesNotExist:
    # If it does not exist, create a new one
    img = Img(name_h='Big_Microgrid')
    img.save()