Scenario Outline: Add new group
  Given a group list
  Given a group with <group_name>, <header_name> and <footer_name>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  | group_name  | header_name  | footer_name  |
  | name1       | header1      | footer1      |
  | name2       | header2      | footer2      |


Scenario: Modify a group
  Given a non-empty group list
  Given index of a random group from the list
  When I modify <name>, <header> and <footer> of the chosen group
  Then the new group list is equal to old group list with modified group

  Examples:
  | name     | header     | footer     |
  | new_name | new_header | new_footer |


Scenario: Delete a group
  Given a non-empty group list
  Given index of a random group from the list
  When I delete the group from the list
  Then the new group list is equal to old group list without the deleted group
