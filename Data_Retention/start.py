from datasessions import session
from data.models import Rule, State, Folder, Violation, Project, Dashboard

# Adding state to state table
state = State(record_time='13:00:00', compare_time='12:00:00')
session.add(state)
session.commit()

# Adding dashboard to dashboard table
dashboard = Dashboard(summary='summary1', states=state)
session.add(dashboard)
session.commit()

# Adding folder to folder table
folder = Folder(name='folder2')
session.add(folder)
session.commit()
folder_list = session.query(Folder).all()
for folder in folder_list:
    state.folders.append(folder)
session.commit()

# Adding rule to rule table
rule = Rule(name='rule2', description='rr')
session.add(rule)
session.commit()
rule_list = session.query(Rule).all()
for rule in rule_list:
    state.rules.append(rule)
session.commit()

# Adding violation to violation table
violation = Violation(name='violation2', description='vv')
session.add(violation)
session.commit()
violation_list = session.query(Violation).all()
for violation in violation_list:
    state.violations.append(violation)
session.commit()

# Adding project to project table
project = Project(name='project2')
session.add(project)
session.commit()
project_list = session.query(Project).all()
for project in project_list:
    state.projects.append(project)
session.commit()

# Counting a row count
row_count = session.query(State).count()

# Calculating remaining rows
rem_rows = session.query(State).limit(row_count - 10).all()

# Un-linking the resources and deleting a resource
for state in rem_rows:
    state.folders = []
    state.rules = []
    state.violations = []
    state.projects = []
    session.commit()
# Un-linking state and and deleting dashboard
    session.query(Dashboard).filter(Dashboard.state_id == state.id).delete()
    qs = session.query(State).filter(State.id == state.id)
    qs.delete(synchronize_session=False)
session.commit()
