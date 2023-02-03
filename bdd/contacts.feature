Scenario Outline: Add new contact
  Given a list of contacts
  Given a new contact with <firstname>, <middlename>, <lastname> and <nickname>
  When I add new contact to the contact list
  Then new contact list is equal to the old contact list with new contact

  Examples:
  | firstname | middlename | lastname | nickname |
  | John      | Adam       | Roberts  | Tiger    |


Scenario: Modify contact
  Given a non-empty list of contacts
  Given index of a random contact from the list
  When a new <firstname>, <middlename>, <lastname> and <nickname> is entered
  Then the new contact list is equal to old contact list with modified contact

  Examples:
  | firstname | middlename | lastname | nickname |
  | Pauline   | Catherine  | Smith    | Daisy    |
  | Peter     | Arnold     | Johnson  | Buddy    |


Scenario: Delete contact
  Given a non-empty list of contacts
  Given index of a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to old contact list without the deleted contact
