from django import forms
from census.models import CensusInfo


class CensusInfoForm(forms.ModelForm):

    class Meta:
        model = CensusInfo
        fields = ['name', 'admin_comments', 'is_accepted', 'address', 'city', 'state', 'phone', 'zip_code',]
