from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic
from .models import Constituencies, Candidates, State, Party, Constituency_State


# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'info/home.html'


class PartyView(generic.TemplateView):
    template_name = 'info/party.html'


class CandidateDetail(generic.DetailView):
    model = Candidates
    template_name = 'info/profile.html'
    context_object_name = 'candidate_object'


class ConstituencyDetail(generic.DetailView):
    model = Constituencies
    template_name = 'info/details.html'
    context_object_name = 'constituency_object'

    def get_context_data(self, **kwargs):
        details_context = super().get_context_data(**kwargs)
        current_constituency = self.get_object()
        candidate_list = Candidates.objects.filter(pincode=current_constituency.pincode,
                                                   constituency=current_constituency.constituency)
        details_context['candidate_list'] = candidate_list
        return details_context


class ResultsView(generic.ListView):
    template_name = 'info/results.html'
    context_object_name = 'results_list'

    def get_queryset(self):
        # print(self.kwargs)
        search_param = self.kwargs['search_param']
        search_key = self.kwargs['search_key']
        if search_param == 'pincode':
            return Constituencies.objects.filter(pincode__startswith=search_key)
        elif search_param == 'state':
            return State.objects.filter(state__startswith=search_key)
        elif search_param == 'constituency':
            return Constituencies.objects.filter(constituency__startswith=search_key)
        elif search_param == 'state-to-constituency':
            self.kwargs['search_param'] = 'constituency'
            search_key = search_key.replace('-',' ')
            return Constituency_State.objects.filter(state__icontains=search_key)
        elif search_param == 'party':
            return Party.objects.filter(party__startswith=search_key)
        elif search_param == 'constituency-to-candidate':
            self.kwargs['search_param'] = 'candidate'
            return Candidates.objects.filter(constituency__startswith=search_key)
        else:
            return Candidates.objects.filter(name__startswith=search_key)

    def get_context_data(self, *, object_list=None, **kwargs):
        results_context = super().get_context_data(object_list=object_list, **kwargs)
        results_context['search_param'] = self.kwargs['search_param']
        results_context['search_key'] = self.kwargs['search_key']
        return results_context


def search_keyword(request):
    search_param = request.POST['search_param']
    search_key = request.POST['search_key']
    print("search_param: ", search_param)
    print("search_key: ", search_key)
    return HttpResponseRedirect(
        reverse('info:results', args=(search_param, search_key,)))
