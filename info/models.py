from django.db import models


# Create your models here.


class Constituencies(models.Model):
    state = models.CharField(max_length=30)
    constituency = models.CharField(max_length=30)
    pincode = models.CharField(max_length=10, primary_key=True)
    upcoming_election_date = models.DateField()
    upcoming_election_type = models.CharField(max_length=30)

    def __str__(self):
        return self.pincode


class Candidates(models.Model):
    state = models.CharField(max_length=30)
    constituency = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    party = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    pincode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    educational_details = models.TextField(blank=True, null=True)
    assets = models.CharField(max_length=30, blank=True, null=True)
    liabilities = models.CharField(max_length=30, blank=True, null=True)
    criminal_cases = models.TextField(blank=True, null=True)
    election_type = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Party(models.Model):
    party = models.CharField(max_length=30)

    def __str__(self):
        return self.party


class State(models.Model):
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.state


class Constituency_State(models.Model):
    constituency = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.constituency
