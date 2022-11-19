from sys import maxsize


class Contact:

    def __init__(self,
                 firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 photo_file_location=None,
                 title=None,
                 company=None,
                 address=None,
                 home_phone=None,
                 mobile_phone=None,
                 work_phone=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 home_page=None,
                 birth_day=None,
                 birth_month=None,
                 birth_year=None,
                 anniversary_day=None,
                 anniversary_month=None,
                 anniversary_year=None,
                 group_name=None,
                 extra_address=None,
                 extra_phone=None,
                 notes=None,
                 id=None
                 ):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo_file_location = photo_file_location
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.home_page = home_page
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.group_name = group_name
        self.extra_address = extra_address
        self.extra_phone = extra_phone
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.group_name)

    def __eq__(self,other):
        # return self.id == other.id and self.firstname == other.middlename and self.lastname == other.lastname
        return (self.id is None or other.id is None) or (self.id == other.id and self.firstname == other.firstname and self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
