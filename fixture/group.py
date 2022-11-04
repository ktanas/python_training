class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element("link text", "groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element("link text", "group page").click()

    def create(self, group):
        # Open groups page
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element("name", "new").click()
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys("%s" % group.group_name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys("%s" % group.header_name)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys("%s" % group.footer_name)
        wd.find_element("name", "submit").click()
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

    def modify_group_name(self, new_name):
        # Edit the group's name. This method assumes that we are already on the group edition page.
        wd = self.app.wd
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys("%s" % new_name)

    def modify_group_header(self, new_header):
        # Edit the group's header. This method assumes that we are already on the group edition page.
        wd = self.app.wd
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys("%s" % new_header)

    def modify_group_footer(self, new_footer):
        # Edit the group's footer. This method assumes that we are already on the group edition page.
        wd = self.app.wd
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys("%s" % new_footer)

    def modify_finalize(self):
        # Click on the "Update" button after finishing modification of the group's data
        wd = self.app.wd
        wd.find_element("name", "update").click()

    def delete_first_group(self):
        # Open groups page
        wd = self.app.wd
        self.open_groups_page()
        # Select first group in the group list
        wd.find_element("name", "selected[]").click()
        # Delete the selected group
        wd.find_element("name","delete").click()
        # Return to group page
        self.return_to_group_page()


