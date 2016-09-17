from django.db import models
from django.db.models import CharField, IntegerField, BooleanField, TextField

class Participant(models.Model):
    name = CharField(max_length=256)
    age = IntegerField()
    has_siblings = BooleanField()
    environmental_exposures = TextField()
    genetic_mutations = TextField()
    
    NOT_REVIEWED = "NR"
    REVIEWED_AND_ACCEPTED = "RA"
    REVIEWED_NOT_ACCEPTED = "RN"
    REVIEW_STATUSES = (
        (NOT_REVIEWED,'Not Reviewed'),
        (REVIEWED_AND_ACCEPTED, 'Reviewed - Accepted'),
        (REVIEWED_NOT_ACCEPTED, 'Reviewed - Not Accepted')
    )
    review_status = CharField(
        max_length=2,
        choices = REVIEW_STATUSES,
        default = NOT_REVIEWED,
    )