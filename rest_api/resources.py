from falcon_autocrud.resource import CollectionResource, SingleResource
from note.models import *


class NoteCollectionResource(CollectionResource):
    model = Note
    methods = ['GET', 'POST']


class NoteResource(SingleResource):
    model = Note
