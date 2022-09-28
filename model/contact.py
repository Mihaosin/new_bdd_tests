from sys import maxsize


class Contact:
    def __init__(self, id=None, lastname=None, firstname=None, address=None,
                 mail1=None, mail2=None, mail3=None, all_mails_from_home_page=None,
                 homephone=None, mobilephone=None, workphone=None, fax=None, all_phones_from_home_page=None):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
        self.mail1 = mail1
        self.mail2 = mail2
        self.mail3 = mail3
        self.all_mails_from_home_page = all_mails_from_home_page
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.all_phones_from_home_page = all_phones_from_home_page

    def __eq__(self, other):
        EQ1 = self.id is None or other.id is None or self.id == other.id
        EQ2 = self.firstname == other.firstname
        EQ3 = self.lastname == other.lastname
        return EQ1 and EQ2 and EQ3

    def id_or_max(self):
        if self.id:
            return  int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s:%s;%s" % (self.id, self.firstname, self.lastname)