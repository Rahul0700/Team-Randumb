from django.shortcuts import render
from accounts.models import GroupMember,Group, QuestionResponse

from .forms import take_question
from .groupping import checkSemantics,load_pretrained,get_embeddings

from django.shortcuts import render
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
from keras.models import load_model
global graph,model




# Create your views here.
def Home(request):
    member_groups = []
    admin_groups = []
    if request.user.is_authenticated:
        member_groups = GroupMember.objects.filter(user=request.user)
        admin_groups = Group.objects.filter(admin=request.user.username)
    return render(request,'home.html',{'member_groups':member_groups,
                                       'admin_groups':admin_groups})



#Assuming data is present
print("Keras model loading.......")
embed = get_embeddings()
model = load_pretrained(embed)
# embeddings = embeddings()
print("Model loaded!!")

def predict(request):
    if request.method == "POST":
        form = take_question(data = request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            print("***************************")
            print(question)
            print("**************************************")
            from_database = QuestionResponse.objects.values('question')
            for i in from_database:
                result = checkSemantics(question, i, model)
                tf.executing_eagerly()
                prediction = model.predict(result)
                print(prediction)
                if prediction == True:
                    res.append(i)
            print(res)
    else:
        form = take_question()
    return render(request,'model.html',{
    "form": form
    })
        # Add the frequency in the questions where the results are True
        #Add the user id in the question as well
        #Return a render to the page saying question sent successfully
