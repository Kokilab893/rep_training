from falcon_autocrud.resource import CollectionResource, SingleResource
from vehicle.models import sessionmaker, db_engine, User, Car
import falcon


class LinkUsertoCar(object):
    def on_post(self, req, resp, *args, **kwargs):
        print(req.context)
        Session = sessionmaker(bind=db_engine)
        session = Session()
        uid = req.context['doc']['User']
        # print(uid)
        cid_list = req.context['doc']['Car']
        cars_list = []
        for cid in cid_list:
            cars_list.append(session.query(Car).filter(Car.id == int(cid)).all()[0])
        user = session.query(User).filter(User.id == int(uid)).all()
        u = user[0]
        # print(u)
        for car in cars_list:
            u.cars.append(car)
        session.commit()


class LinkCartoUser(object):
    def on_post(self, req, resp, *args, **kwargs):
        print(req.context)
        cid = req.context['doc']['Car']
        print(cid)
        uid_list = req.context['doc']['User']
        Session = sessionmaker(bind=db_engine)
        session = Session()
        users_list = []
        for uid in uid_list:
            users_list.append(session.query(User).filter(User.id == int(uid)).all()[0])

        car = session.query(Car).filter(Car.id == int(cid)).all()
        c = car[0]
        print(c)
        for user in users_list:
            c.users.append(user)
        session.commit()


class UserCollectionResource(CollectionResource):
    model = User
    methods = ['GET', 'POST']
    allow_subresources = True


class UserResource(SingleResource):
    model = User


class CarCollectionResource(CollectionResource):
    model = Car
