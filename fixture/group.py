from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements("link text", "New group")) > 0):
            wd.find_element("link text", "groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element("link text", "group page").click()

    def create(self, group):
        # Open groups page
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element("name", "new").click()

        self.set_field_value("group_name", group.group_name)
        self.set_field_value("group_header", group.header_name)
        self.set_field_value("group_footer", group.footer_name)

        wd.find_element("name", "submit").click()
        # Return to group page
        self.return_to_group_page()

    def set_field_value(self, field_name, text):
        wd = self.app.wd
        wd.find_element("name", field_name).click()
        wd.find_element("name", field_name).clear()
        wd.find_element("name", field_name).send_keys("%s" % text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys("%s" % text)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.group_name)
        self.change_field_value("group_header", group.header_name)
        self.change_field_value("group_footer", group.footer_name)

    def modify_first_group(self, new_group_data):
        wd = self.app.wd

        # Open page containing list of groups
        self.open_groups_page()
        # Select the first group from list
        self.select_first_group()
        # Open modification form
        wd.find_element("name", "edit").click()
        # Fill group form
        self.fill_group_form(new_group_data)
        # Submit modification
        wd.find_element("name", "update").click()
        # Return to group page
        self.return_to_group_page()

    def modify_initialize(self):
        # Open page containing list of groups
        wd = self.app.wd
        self.open_groups_page()
        # Find group to modify - click on the group with given name
        # wd.find_element("title", "Select ("+ group_name +")").click()
        wd.find_element("name", "selected[]").click()
        # Click on the 'Edit group' button
        wd.find_element("name", "edit").click()

    def modify_finalize(self):
        # Click on the "Update" button after finishing modification of the group's data
        wd = self.app.wd
        wd.find_element("name", "update").click()

    def delete_first_group(self):
        # Open groups page
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # Delete the selected group
        wd.find_element("name", "delete").click()
        # Return to group page
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        # Select first group in the group list
        wd.find_element("name", "selected[]").click()

    def count(self):
        # Return number of currently existing groups
        wd = self.app.wd
        return len(wd.find_elements("name", "selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        group_list = []
        for element in wd.find_elements("css selector", "span.group"):
            text = element.text
            element.find_element("name", "selected[]").get_attribute("value")
            group_list.append(Group(group_name=text, id=id))
        return group_list
