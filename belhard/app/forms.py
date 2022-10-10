from django.forms import Form, IntegerField


class Calculator(Form):
    width = IntegerField(min_value=1)
    height = IntegerField(min_value=1)
