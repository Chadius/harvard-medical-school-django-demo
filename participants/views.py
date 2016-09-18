from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Participant

def get_participant_choices():
    participant_review_status_choices = {}
    for status_group in Participant.REVIEW_STATUSES:
        participant_review_status_choices[status_group[0]] = status_group[1]
    return participant_review_status_choices

def index(request):
    participants_to_view = Participant.objects.all
    participant_review_status_choices = get_participant_choices()

    return render(
        request, 
        'participants/index.html', 
        {
            'participant_review_status_choices' : participant_review_status_choices.items(),
            'participants': participants_to_view,
        }
    )

def new(request):
    return render(
        request, 
        'participants/new.html', 
    )

def save(request):
    # Get fields from request
    new_fields = {}
    
    # Enforce the name and age fields are not blank.
    required_fields = {
        'name' : {
            'key' : "name",
            'error_message' : "Name is required.",
        },
        'age' : {
            'key' : "age",
            'error_message' : "Age is required.",
        }
    }

    for k in required_fields:
        new_fields[required_fields[k]['key']] = request.POST[required_fields[k]['key']]
        if not new_fields[required_fields[k]['key']]:
            return render(request, 'participants/new.html', {
                'error_message': new_fields[required_fields[k]['error_message']]
            })

    new_fields['has_siblings'] = request.POST.get('has_siblings', False)
    new_fields['environmental_exposures'] = request.POST.get('environmental_exposures', None)
    new_fields['genetic_mutations'] = request.POST.get('genetic_mutations', None)
    
    # Try to make a new participant
    new_participant = Participant.objects.create(
        name = new_fields['name'],
        age = new_fields['age'],
        has_siblings = new_fields['has_siblings'],
        environmental_exposures = new_fields['environmental_exposures'],
        genetic_mutations = new_fields['genetic_mutations'],
    )
    
    new_participant.save()
    
    # redirect to the index page
    return HttpResponseRedirect(
        reverse('participants:index')
    )

def update_review(request, participant_id):
    # Get participant
    participant_to_update = None
    participants_to_view = Participant.objects.all
    participant_review_status_choices = get_participant_choices()
    
    try:
        participant_to_update = Participant.objects.get(pk=participant_id)
    except (Participant.DoesNotExist):
        return render(request, 'participants/index.html', {
            'error_message': 'Participant does not exist.',
            'participants': participants_to_view,
            'participant_review_status_choices' : participant_review_status_choices.items,
        })
    
    # Get the field
    new_review_status = None
    try:
        new_review_status = request.POST['review_status']
    except (KeyError):
        return render(request, 'participants/index.html', {
            'error_message': 'Status does not exist.',
            'participants': participants_to_view,
            'participant_review_status_choices' : participant_review_status_choices.items,
        })

    # Update the field
    participant_to_update.review_status = new_review_status

    # Save the participant
    participant_to_update.save()

    # redirect to index page
    return HttpResponseRedirect(
        reverse('participants:index')
    )