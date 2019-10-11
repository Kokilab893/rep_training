from sqlalchemy import create_engine
import falcon
from vehicle.models import db_engine
from vehicle.resources import UserCollectionResource, UserResource, CarCollectionResource
from note.resources import LinkUsertoCar, LinkCartoUser, UnLinkUsertoCar
from falcon_autocrud.middleware import Middleware

app = falcon.API(
    middleware=[Middleware()],
)

app.add_route('/users', UserCollectionResource(db_engine))
app.add_route('/users/{uid}', UserResource(db_engine))
app.add_route('/cars/', CarCollectionResource(db_engine))
app.add_route('/LinkUsertoCar', LinkUsertoCar())
app.add_route('/LinkCartoUser', LinkCartoUser())
app.add_route('/UnLinkUsertoCar', UnLinkUsertoCar())
# app.add_route('/UnLinkCartoUser',UnLinkCartoUser)
