# Issue


class Issue:
    def __init__(self, dir, num):
        self.directory = dir
        self.issue_number = num
        self.get_main()
        self.get_notes()
        self.get_replies()
        self.get_audit()
    
    def json(self):
        return self.__dict__

    def get_main(self):
        pass

    def get_notes(self):
        pass

    def get_replies(self):
        pass

    def get_audit(self):
        pass