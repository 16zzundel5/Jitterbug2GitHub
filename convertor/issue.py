# Issue
import os

class Issue:
    def __init__(self, dir, num):
        self.directory = dir
        self.issue_number = num
        self._get_main()
        self._get_notes()
        self._get_replies()
        self._get_audit()
        self._get_followups()

        self._parse_notes

    def _get_main(self):
        self.main = self._get_single_file()

    def _get_notes(self):
        self.notes = self._get_single_file("notes")

    def _get_replies(self):
        self.replies = self._get_multiple_file("reply")

    def _get_audit(self):
        self.audit = self._get_single_file("audit")

    def _get_followups(self):
        self.followups = self._get_multiple_file("followup")

    def _get_single_file(self, suffix=None):
        path = ""

        if suffix is not None:
            path = os.path.join(self.directory, self.issue_number + "." + suffix)
        else:
            path = os.path.join(self.directory, self.issue_number)
        
        try:
            with open(path) as f:
                return f.read()
        except IOError:
            return ""

    def _get_multiple_file(self, suffix):
        files = []
        num = 1
        while True:
            if not os.path.exists(os.path.join(self.directory, self.issue_number + "." + suffix + "." + str(num))):
                break

            files.append(self._get_single_file(suffix + "." + str(num)))
            
            num += 1
        
        return files

    def _parse_notes(self):
        notes = self.notes
        
