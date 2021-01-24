from django.db import models

from blood.models.base import DomainEntity
from blood.models.location import Location
from blood.utils import SelectGender, BloodGroup


class Donor(DomainEntity):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.TextField()
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, related_name='donor_location')
    select_blood = models.CharField(max_length=3, choices=BloodGroup.choices, default=BloodGroup.AB)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.IntegerField(choices=SelectGender.select_gender(), default=SelectGender.MALE.value)
    profession = models.CharField(max_length=100, blank=True, null=True)
    last_donation_date = models.DateField(null=True)


    def __str__(self):
        return self.first_name[:20]
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    