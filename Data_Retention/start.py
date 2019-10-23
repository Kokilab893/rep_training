from datasessions import session
from data.models import Rule, State, Folder, Violation, Project, Dashboard, states_violations, states_rules
from sqlalchemy import func, desc

# Adding state to state table
state = State(record_time='09:00:00', compare_time='08:00:00')
session.add(state)
session.commit()

# Adding dashboard to dashboard table
dashboard = Dashboard(summary='summary1', states=state)
session.add(dashboard)
session.commit()

# Adding folder to folder table
folder = Folder(name='folder1')
session.add(folder)
session.commit()
folder_list = session.query(Folder).all()
for folder in folder_list:
    state.folders.append(folder)
session.commit()

# Adding rule to rule table
rule = Rule(name='rule1', description='rrrrr')
session.add(rule)
session.commit()
rule_list = session.query(Rule).all()
for rule in rule_list:
    state.rules.append(rule)
session.commit()

# Adding violation to violation table
violation = Violation(name='violation1', description='vvvvv')
session.add(violation)
session.commit()
violation_list = session.query(Violation).all()
for violation in violation_list:
    state.violations.append(violation)
session.commit()

# Adding project to project table
project = Project(name='project1')
session.add(project)
session.commit()
project_list = session.query(Project).all()
for project in project_list:
    state.projects.append(project)
session.commit()

# Counting a row count
# row_count = session.query(State).count()
#
# # Calculating remaining rows
# rem_rows = session.query(State).limit(row_count - 10).all()
#
# # Un-linking the resources and deleting a resource
# for state in rem_rows:
#     state.folders = []
#     state.rules = []
#     state.violations = []
#     state.projects = []
#     session.commit()
# #     #     # Un-linking state with dashboard and and deleting dashboard
#     session.query(Dashboard).filter(Dashboard.state_id == state.id).delete()
#     qs = session.query(State).filter(State.id == state.id)
#     qs.delete(synchronize_session=False)
# session.commit()
#
# Inner join usage
# result = session.query(states_violations,Violation.id).join(Violation)
# result=result.all()
# print(result)
#
# # Left_Outer_Join usage
# result = session.query(states_violations, Violation.id).outerjoin(Violation).all()
# print(result)

# Calculating total count of a projects
# project_count = session.query(func.count(Project.id)).all()
# print(project_count)

# Calculating minimum no.of project
# project_min = session.query(func.min(Project.id)).all()
# print(project_min)

# Calculating maximum no.of projects
# project_max = session.query(func.max(Project.id)).all()
# print(project_max)

# Group_by with name
# qs = session.query(func.count(Project.id)).group_by(Project.name).all()
# print(qs)

# Order_by with the violation name
# qs = session.query(Violation.name).order_by(Violation.name.desc())
# result = qs.all()
# print(result)

# qs = session.query(State.record_time, func.count(Rule.id), func.count(Violation.id)).join(states_violations).join(
#     Violation).join(
#     states_rules).join(Rule).group_by(State.record_time)
# result = qs.all()
# print(qs)

# Joining multiple tables with multiple selecters
qs = session.query(State).join(states_violations).join(Violation).join(states_rules).join(Rule)
qs1 = qs.with_entities(State.id, func.count(Rule.id), func.count(Violation.id)).group_by(State.id)
result = qs1.all()
print(result)

