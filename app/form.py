from django.forms import ModelForm

from app.models import User


class UserModelForm(ModelForm):

    class Meta:
        model = User
        fields = '__all__'
