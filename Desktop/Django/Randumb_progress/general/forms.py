from django.forms import ValidationError,EmailField,ModelForm
from accounts.models import QuestionResponse



class take_question(ModelForm):
    class Meta:
        field = ("question")
        exclude = ("is_response","response","frequency")
        model = QuestionResponse
