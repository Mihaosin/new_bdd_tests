#Scenario Outline: Add new group
#  Given a group list
#  When I add a new group to the list
#  Then the new group list is equal to the old list with added group


Scenario: Add new group
Given a group list
Given a group with name, header and footer
When I add the group to the list
Then the new group list is equal to the old list with the added group

#Examples:
#| name  | header  | footer  |
#| name1 | header1 | footer1 |