from django.shortcuts import get_list_or_404, render,  redirect
from django.views import generic
from .models import Event

class IndexView(generic.ListView):
    template_name = 'Event/index.html'
    paginate_by = 100  # if pagination is desired
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        return Event.objects.order_by('-dateDebut')


class DetailView(generic.DetailView):
    model = Event
    template_name = 'Event/detail.html'

"""def index(request):
    latest_event_list = Event.objects.all()
    return render(request, 'Event/home.html', {'latest_event_list': latest_event_list})

def detail(request, id_event):
    event = get_object_or_404(Question, pk=id_event)
    return render(request, 'Event/detail.html', {'event': event})"""
