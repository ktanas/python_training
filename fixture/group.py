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
        self.group_cache = None

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

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd

        # print("modify_group_by_index: index="+str(index))

        # Open page containing list of groups
        self.open_groups_page()
        # Select group with the given index on the group list
        self.select_group_by_index(index)
        # Open modification form
        wd.find_element("name", "edit").click()
        # Fill group form
        self.fill_group_form(new_group_data)
        # Submit modification
        wd.find_element("name", "update").click()
        # Return to group page
        self.return_to_group_page()
        self.group_cache = None

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)

    def modify_initialize(self, index):
        # Open page containing list of groups
        wd = self.app.wd
        self.open_groups_page()
        # Find group to modify - click on the group with given name
        # wd.find_element("title", "Select ("+ group_name +")").click()
        wd.find_elements("name", "selected[]")[index].click()
        # Click on the 'Edit group' button
        wd.find_elements("name", "edit")[index].click()

    def modify_finalize(self):
        # Click on the "Update" button after finishing modification of the group's data
        wd = self.app.wd
        wd.find_element("name", "update").click()

    def delete_group_by_index(self, index):
        # Open groups page
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # Delete the selected group
        wd.find_element("name", "delete").click()
        # Return to group page
        self.return_to_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        # Select group with the given index from the group list
        wd.find_elements("name", "selected[]")[index].click()

    def select_first_group(self):
        self.select_group_by_index(0)

    def count(self):
        # Return number of currently existing groups
        wd = self.app.wd
        return len(wd.find_elements("name", "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements("css selector", "span.group"):
                text = element.text
                id = element.find_element("name", "selected[]").get_attribute("value")
                self.group_cache.append(Group(group_name=text, id=id))

        return list(self.group_cache)

