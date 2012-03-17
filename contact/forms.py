# -*- coding: UTF-8 -*-
from django import forms
from contact.models import ContactInfo


class ContactInfoForm(forms.ModelForm):

    class Meta:
        model = ContactInfo
        fields = ['name', 'address', 'city', 'state', 'phone', 'zip_code', 'subject', 'question']
