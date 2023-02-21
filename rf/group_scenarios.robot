*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create group  ${group}
    ${new_list}=  Get Group List
    Append To List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Modify_group
    Make sure that group list is not empty
    ${old_list}=  Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  Get From List  ${old_list}  ${index}
    ${new_group} =  New Group  name2  header2  footer2
    Enter new group data  ${index}  ${new_group}
    ${new_list}=  Get Group List
    Set List Value  ${old_list}  ${index}  ${new_group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Delete group
    Make sure that group list is not empty
    ${old_list}=  Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  Get From List  ${old_list}  ${index}
    Delete group  ${group}
    ${new_list}=  Get Group List
    Remove Values From List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}
