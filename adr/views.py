from django.shortcuts import render
from adr.models import Neutral, Inquiry
from django.views import generic

# Create your views here.
def index(request):
    num_inquiry = Inquiry.objects.count()
    #num_confirmed = Inquiry.objects.filter(confirmed).count()
    #num_follow1 = Inquiry.objects.filter(follow1).count()
    #num_follow2 = Inquiry.objects.filter(follow2).count()
    #num_closed = Inquiry.objects.filter(closed).count()
    
    context = {
        'num_inquiry' : num_inquiry,
        #'num_confirmed' : num_confirmed,
        #'num_follow1' : num_follow1,
        #'num_follow2' : num_follow2,
        #'num_closed' : num_closed,
    }
    
    return render(request, 'index.html', context=context)

class InquiryListView(generic.ListView):
    model = Inquiry
    def get_queryset(self):
        return Inquiry.objects.filter('confirmed').count()

