import os
import datetime
import calendar

class Migrator(object):
    def __init__(self, migrations_directory):
        self.migrations_directory = migrations_directory
        pass

    def init(self):
        if os.path.exists(self.migrations_directory):
            print '"%s" already exists' % self.migrations_directory
        else:
            os.makedirs(self.migrations_directory)

    def create_migration(self, migration_name):
        timestamp = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

        file_name = '_'.join([str(timestamp), ('%s.py' % migration_name)])
        print os.path.join(self.migrations_directory, file_name)

