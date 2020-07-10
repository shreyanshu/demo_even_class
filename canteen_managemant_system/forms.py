from django import forms
from canteen_managemant_system.models import FoodItem, Cook, CookInfo


class FoodItemForm(forms.Form):
    name = forms.CharField()
    price = forms.IntegerField()
    qty = forms.IntegerField()
    discount = forms.FloatField()


class FoodItemModelForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        # fields = ('name', 'price', 'discount')
        fields = '__all__'


class InfoModelForm(forms.ModelForm):
    class Meta:
        model = CookInfo
        fields = '__all__'


class CookModelForm(forms.ModelForm):
    phone_no = forms.CharField(max_length=12)
    pan_no = forms.IntegerField()

    class Meta:
        model = Cook
        # exclude = ('info', )
        fields = ('name', 'age', 'profile_pic')

    def save(self, commit=True):
        cook = super(CookModelForm, self).save()
        cook.info = CookInfo.objects.create(phone_no=self.cleaned_data.get('phone_no'),
                                            pan_no=self.cleaned_data.get('pan_no'))
        cook.save()
        return cook

    def __init__(self, *args, **kwargs):
        super(CookModelForm, self).__init__(*args, **kwargs)
        if kwargs.get('instance') is not None:
            if kwargs.get('instance').info is not None:
                self.fields['phone_no'].initial = kwargs.get('instance').info.phone_no
                self.fields['pan_no'].initial = kwargs.get('instance').info.pan_no


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


