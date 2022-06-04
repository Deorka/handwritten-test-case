import datetime
import os
import psutil
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        try:
            self.prep()
            logger.info(f'Test №{self.tc_id} {self.name} fun "prep" is passed')
        except AssertionError:
            logger.warning(f'Test №{self.tc_id} {self.name} fun "prep" is aborded. Fun "run" is skipped')
        except Exception:
            logger.error(f'Test №{self.tc_id} {self.name} unexpected error')
        else:
            self.run()
            logger.info(f'Test №{self.tc_id} {self.name} fun "run" is passed')
        finally:
            self.clean_up()
            logger.info(f'Test №{self.tc_id} {self.name} fun "clean_up" is passed')


class TestCaseListFiles(TestCaseBase):
    def prep(self):
        seconds_from_epoch = int(datetime.datetime.timestamp(datetime.datetime.now()))
        assert seconds_from_epoch % 2

    def run(self):
        print(os.listdir(path="/"))


class TestCaseRandomFile(TestCaseBase):
    def prep(self):
        virtual_memory = psutil.virtual_memory().total
        assert virtual_memory >= 1024*1024*1024

    def run(self):
        with open('test', 'wb') as out:
            out.write(os.urandom(1024))

    def clean_up(self):
        os.remove('test')


if __name__ == '__main__':
    TestCaseListFiles(1, 'TestCaseRandomFile').execute()
    TestCaseRandomFile(2, 'TestCaseRandomFile').execute()
