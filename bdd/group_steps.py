# from pytest_bdd import given, when, then
# from model.group import Group
#
# @given('a group list')
# def group_list(app):
#     return app.group.get_group_list()
#
# # @given('a group with <name>, <header> and <footer>')
# # def new_group(name, header, footer):
# #     return Group(name=name, header=header, footer=footer)
#
# @when('I add a new group to the list')
# def add_new_group(app):
#     new_group = Group(name='name', header='header', footer='footer')
#     app.group.create(new_group)
#     return new_group
#
# @then('the new group list is equal to the old list with added group')
# def verify_group_added(app, group_list, add_new_group):
#     old_groups = group_list
#     new_group = add_new_group
#     new_groups = app.group.get_group_list()
#     old_groups.append(new_group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


from pytest_bdd import given, when, then
from model.group import Group
import random

group_list = None
new_group = None

@given('a group list')
def group_list(app):
    global group_list
    group_list = app.group.get_group_list()
   # return app.group.get_group_list()

@given('a group with name, header and footer')
def new_group():
    global new_group
    new_group = Group(name="name", header="header", footer="footer")
    # return Group(name="name", header="header", footer="footer")

@when('I add the group to the list')
def add_new_group(app):
    global new_group
    app.group.create(new_group)

@then('the new group list is equal to the old list with the added group')
def verify_group_added(app):
    global group_list
    global new_group
    old_groups = group_list
    new_groups = app.group.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
