from django.shortcuts import render
from accounts.models import GroupMember,Group
# Create your views here.
def Home(request):
    member_groups = []
    admin_groups = []
    if request.user.is_authenticated:
        member_groups = GroupMember.objects.filter(user=request.user)
        admin_groups = Group.objects.filter(admin=request.user.username)
    return render(request,'home.html',{'member_groups':member_groups,
                                       'admin_groups':admin_groups})
