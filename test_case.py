import datetime
import os
import psutil
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
        else:
            if self.prep() == 'aborted':
                pass  # run and cleap_up is skipped


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
        virtual_memory = psutil.virtual_memory().total
        if virtual_memory < 1024*1024*1024:
            return 'aborted'
        else:
            return 'completed'

    def run(self):
        with open('test', 'wb') as out:
            out.write(os.urandom(1024))

    def clean_up(self):
        os.remove('test')


if __name__ == '__main__':
    print(TestCaseRandomFile(1, 'prep').run())
