from django.shortcuts import render
from accounts.models import GroupMember,Group
from .models import Event,FAQ
from django.contrib.auth.decorators import login_required
from .forms import eventForm,questionForm
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def Home(request):
    member_groups = []
    admin_groups = []
    if request.user.is_authenticated:
        member_groups = GroupMember.objects.filter(user=request.user)
        admin_groups = Group.objects.filter(admin=request.user.username)
    return render(request,'home.html',{'member_groups':member_groups,
                                       'admin_groups':admin_groups})

@login_required
def Eventform(request,slug):
    if request.method == 'POST':
        form = eventForm(data=request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.group = Group.objects.get(slug=slug)
            event.save()
            return HttpResponseRedirect(reverse('general:event',kwargs={"id":event.id}))
    else:
        form = eventForm()
    return render(request,'accounts/form.html',{'form':form})

@login_required
def EventUpdateform(request,id):
    event = Event.objects.get(id=id)
    if request.method == 'POST':
        form = eventForm(data=request.POST,instance=event)
        if form.is_valid():
            event.save()
            return HttpResponseRedirect(reverse('general:event',kwargs={"id":event.id}))
    else:
        form = eventForm(instance=event)
    return render(request,'accounts/form.html',{'form':form})

@login_required
def Eventview(request,id):
    event = Event.objects.get(id=id)
    try:
        faqs = FAQ.objects.filter(event=event)
    except:
        faqs = []
    if request.method == 'POST':
        form = questionForm(data=request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.event = event
            faq.user = request.user
            faq.save()
            return HttpResponseRedirect(reverse('general:event',kwargs={"id":event.id}))
    else:
        form = questionForm()
    return render(request, "general/eventview.html",{'event':event,'faqs':faqs,'form':form})

@login_required
def Eventdelete(request,id):
    event = Event.objects.get(id=id)
    group =event.group
    event.delete()
    return HttpResponseRedirect(reverse('accounts:group',kwargs={"slug":group.slug}))

@login_required
def AnswerFaq(request,id):
    faq = FAQ.objects.get(id=id)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        faq.answer = answer
        faq.save()
        return HttpResponseRedirect(reverse('general:event',kwargs={"id":faq.event.id}))
    return render(request, "general/answerfaq.html",{'faq':faq})
