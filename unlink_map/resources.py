from falcon_autocrud.resource import CollectionResource, SingleResource
from vehicle.models import sessionmaker, db_engine, User, Car


class LinkUsertoCar(object):
    def on_post(self, req, resp, *args, **kwargs):
        print(req.context)
        Session = sessionmaker(bind=db_engine)
        session = Session()
        uid = req.context['doc']['User']
        cid_list = req.context['doc']['Car']
        user = session.query(User).filter(User.id == int(uid)).one()
        for cid in cid_list:
            val = session.query(Car).filter(Car.id == int(cid)).one()[0]
            user.cars.append(val)
        session.commit()


class LinkCartoUser(object):
    def on_post(self, req, resp, *args, **kwargs):
        print(req.context)
        Session = sessionmaker(bind=db_engine)
        session = Session()
        cid = req.context['doc']['Car']
        uid_list = req.context['doc']['User']
        car = session.query(Car).filter(Car.id == int(cid)).one()
        for uid in uid_list:
            val = session.query(User).filter(User.id == int(uid)).one()
            car.users.append(val)
        session.commit()


class UnLinkUsertoCar(object):
    def on_post(self, req, resp, *args, **kwargs):
        print(req.context)
        Session = sessionmaker(bind=db_engine)
        session = Session()
        uid = req.context['doc']['User']
        print(uid)
        cid_list = req.context['doc']['Car']
        cars_list = []
        for cid in cid_list:
            cars_list.append(session.query(Car).filter(Car.id == int(cid)).all()[0])
        user = session.query(User).filter(User.id == int(uid)).all()
        users = user[0]
        print(users)
        for car in cars_list:
            users.cars.remove(car)
        session.commit()


class UserCollectionResource(CollectionResource):
    model = User
    methods = ['GET', 'POST']
    allow_subresources = True


class UserResource(SingleResource):
    model = User


class CarCollectionResource(CollectionResource):
    model = Car
