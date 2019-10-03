from falcon_autocrud.resource import CollectionResource, SingleResource

import falcon
from vehicle.models import User, Car
from session import session


class LinkUsertoCar(object):
    def on_post(self, req, resp, *args, **kwargs):
        uid = req.context['doc']['User']
        user = session.query(User).filter(User.id == int(uid)).one()
        cid_list = req.context['doc']['Car']
        for cid in cid_list:
            try:
                with session.begin_nested():
                    car = session.query(Car).filter(Car.id == int(cid)).one()
                    user.cars.append(car)
            except Exception as e:
                raise falcon.HTTPBadRequest("User:%s" % uid, "is linking with Car: %s" % cid)

        session.commit()


class LinkCartoUser(object):
    def on_post(self, req, resp, *args, **kwargs):
        cid = req.context['doc']['Car']
        car = session.query(Car).filter(Car.id == int(cid)).one()
        uid_list = req.context['doc']['User']
        for uid in uid_list:
            try:
                with session.begin_nested():
                    user = session.query(User).filter(User.id == int(uid)).one()
                    car.users.append(user)
            except Exception as e:
                raise falcon.HTTPBadRequest("Car:%s" % cid, "is linking with User: %s" % uid)
        session.commit()


class UnLinkUsertoCar(object):
    def on_post(self, req, resp, *args, **kwargs):
        uid = req.context['doc']['User']
        user = session.query(User).filter(User.id == int(uid)).one()
        cid_list = req.context['doc']['Car']
        for cid in cid_list:
            try:
                with session.begin_nested():
                    car = session.query(Car).filter(Car.id == int(cid)).one()
                    user.cars.remove(car)
            except Exception as e:
                raise falcon.HTTPBadRequest("User:%s" % uid, "is not linking with Car: %s" % cid)

        session.commit()


class UnLinkCartoUser(object):
    def on_post(self, req, resp, *args, **kwargs):
        cid = req.context['doc']['Car']
        car = session.query(Car).filter(Car.id == int(cid)).one()
        uid_list = req.context['doc']['User']
        for uid in uid_list:
            try:
                with session.begin_nested():
                    user = session.query(User).filter(User.id == int(uid)).one()
                    car.users.remove(user)

            except Exception as e:
                raise falcon.HTTPBadRequest("Car:%s" % cid, "is not linking with User: %s" % uid)
        session.commit()


class UserCollectionResource(CollectionResource):
    model = User
    methods = ['GET', 'POST']
    allow_subresources = True


class UserResource(SingleResource):
    model = User


class CarCollectionResource(CollectionResource):
    model = Car


class CarResource(SingleResource):
    model = Car
