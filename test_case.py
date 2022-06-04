import datetime
import os
import logging


class TestCaseBase:
    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    def prep(self):
        pass

    def run(self):
        pass

    def clean_up(self):
        pass

    def execute(self):
        if self.prep() == 'completed':
            self.run()
            self.clean_up()
        if self.prep() == 'aborted':
            pass


class TestCaseListFiles(TestCaseBase):
    def prep(self):
        seconds_from_epoch = int(datetime.datetime.timestamp(datetime.datetime.now()))
        if seconds_from_epoch % 2:
            return 'aborted'
        else:
            return 'completed'

    def run(self):
        print(os.listdir(path="/"))


class TestCaseRandomFile(TestCaseBase):
    def prep(self):
        pass

    def run(self):
        with open("test", "wb") as out:
            out.truncate(1024)


if __name__ == '__main__':
    TestCaseRandomFile(1, 'prep').run()
