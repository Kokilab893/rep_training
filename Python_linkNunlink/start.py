from datasessions import session
from data.models import State, Project, Folder, Rule, Violation

# Adding folders to Folder table and # Linking Folders to States....
# folder = Folder(name='folder11')
# session.add(folder)
# session.commit()
# state_list = session.query(State).all()
# for state in state_list:
#     folder.states.append(state)
# session.commit()

# UnLinking States to Folders  ....
# state = session.query(State).filter(State.id == 1).one()
# state.folders = []
# session.add(state)
# session.commit()

# Deleting a resource after un-linking....
# qs = session.query(State).filter(State.id.in_(([1])))
# qs.delete(synchronize_session=False)
# session.commit()


# Adding states to State table
# state = State(record_time='13:00:00', compare_time='12:00:00')
# session.add(state)
# session.commit()

# Adding Rules to Rule table and Linking a resource....
# rule = Rule(name='rule12', description='uuuuuuuuuuu')
# session.add(rule)
# session.commit()
# rule_list = session.query(Rule).all()
# for rule in rule_list:
#     state.rules.append(rule)
# session.commit()

# Unl-inking States to Projects.....
# state = session.query(State).filter(State.id == 14).one()
# state.rules = []
# session.add(state)
# session.commit()

# Deleting a resource after un-linking....
# qs = session.query(State).filter(State.id.in_(([14])))
# qs.delete(synchronize_session=False)
# session.commit()


# Adding violations to Violation table and Linking resource....
# violation = Violation(name = 'Violation12', description = 'vvvvvvvvvvvvv')
# session.add(violation)
# session.commit()
# violation_list = session.query(Violation).all()
# for violation in violation_list:
#     state.violations.append(violation)
# session.commit()

# Unl-inking States to Violations.....
# state = session.query(State).filter(State.id == 1).one()
# state.violations = []
# session.add(state)
# session.commit()

# Deleting a resource after un-linking....
# qs = session.query(State).filter(State.id.in_(([1])))
# qs.delete(synchronize_session=False)
# session.commit()


# Adding projects to Project table....
# project = Project(name='projects11')
# session.add(project)
# session.commit()

# Linking Project to States.....
# project = Project(name='aaa111')
# session.add(project)
# session.commit()
# state_list = session.query(State).all()
# for state in state_list:
#     project.states.append(state)
# session.commit()

# UnLinking Project to States....
# project = session.query(Project).filter(Project.id==11).one()
# project.states = []
# session.add(project)
# session.commit()

# Deleting an un-linking source....
# session.query(Project).filter(Project.id==11).delete()
# session.commit()


# Updating project name
# session.query(Project).filter(Project.id == 3).update({'name': 'project3'}, synchronize_session=False)
# session.commit()
