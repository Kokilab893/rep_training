from falcon_autocrud.resource import CollectionResource, SingleResource
from note.models import *


class NoteCollectionResource(CollectionResource):
    model = Note
    methods = ['GET', 'POST']
    allow_subresources = True


class NoteResource(SingleResource):
    model = Note


class BookCollectionResource(CollectionResource):
    model= Book
