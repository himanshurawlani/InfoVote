from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Constituencies, Candidates, State, Party, Constituency_State


# Register your models here.

@admin.register(Constituencies)
class ConstituenciesAdmin(ImportExportModelAdmin):
    list_display = ('pincode', 'state', 'constituency', 'upcoming_election_date', 'upcoming_election_type')
    search_fields = ['pincode', 'upcoming_election_date', 'upcoming_election_type']
    list_filter = ('upcoming_election_type', 'constituency')


@admin.register(Candidates)
class CandidatesAdmin(ImportExportModelAdmin):
    list_display = ('state', 'constituency', 'name', 'party', 'pincode')
    search_fields = ['constituency', 'party']
    list_filter = ('state', 'constituency')


@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    list_display = ('state',)
    search_fields = ['state']
    list_filter = ('state',)


@admin.register(Party)
class PartyAdmin(ImportExportModelAdmin):
    list_display = ('party',)
    search_fields = ['party']
    list_filter = ('party',)

@admin.register(Constituency_State)
class ConstituencyStateAdmin(ImportExportModelAdmin):
    list_display = ('constituency', 'state')
    search_fields = ['constituency', 'state']
    list_filter = ('constituency', 'state')