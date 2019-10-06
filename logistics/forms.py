from django import forms
from .models import Stock, StaffSchedule, Distribution

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('base', 'food','quantity', 'date')

class StaffScheduleForm(forms.ModelForm):
    class Meta:
        model = StaffSchedule
        fields = ('staff', 'task','start', 'end')

class DistributionForm(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = ('name', 'quantity', 'ship_from', 'ship_to', 'staff')
