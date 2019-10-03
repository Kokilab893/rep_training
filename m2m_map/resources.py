from falcon_autocrud.resource import CollectionResource, SingleResource

from vehicle.models import sessionmaker, db_engine, User, Car
from session import session

class LinkUsertoCar(object):
    def on_post(self, req, resp, *args, **kwargs):
        uid = req.context['doc']['User']
        users = session.query(User).filter(User.id == int(uid)).one()
        cid_list = req.context['doc']['Car']
        for cid in cid_list:
            user = session.query(Car).filter(Car.id == int(cid)).one()
            users.cars.append(user)
        session.commit()


class LinkCartoUser(object):
    def on_post(self, req, resp, *args, **kwargs):
        cid = req.context['doc']['Car']
        cars = session.query(Car).filter(Car.id == int(cid)).one()
        uid_list = req.context['doc']['User']
        for uid in uid_list:
            car = session.query(User).filter(User.id == int(uid)).one()
            cars.users.append(car)
        session.commit()

class UnLinkUsertoCar(object):
    def on_post(self, req, resp, *args, **kwargs):
        uid = req.context['doc']['User']
        users = session.query(User).filter(User.id == int(uid)).one()
        cid_list = req.context['doc']['Car']
        for cid in cid_list:
            user = session.query(Car).filter(Car.id == int(cid)).one()
            users.cars.remove(user)
        session.commit()


class UnLinkCartoUser(object):
    def on_post(self, req, resp, *args, **kwargs):
        cid = req.context['doc']['Car']
        cars = session.query(Car).filter(Car.id == int(cid)).one()
        uid_list = req.context['doc']['User']
        for uid in uid_list:
            car = session.query(User).filter(User.id == int(uid)).one()
            cars.users.remove(car)
        session.commit()


class UserCollectionResource(CollectionResource):
    model = User
    methods = ['GET', 'POST']
    allow_subresources = True


class UserResource(SingleResource):
    model = User


class CarCollectionResource(CollectionResource):
    model = Car

