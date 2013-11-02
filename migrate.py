from options import Options
from migrate.migrator import Migrator
from migrate.migration import Migration

migrate = Migrator('db/migrate')

# python migrate.py --init
# python migrate.py --create-migration create_users
options = Options()
options.add('--init', migrate.init)
options.add('--migrate', 'migrate')
options.add('--rollback', 'rollback')
options.add('--create-migration', migrate.create_migration)
options.add('--remove-migration', 'remove_migration')
options.add('--load-schema', 'load_schema')
options.add('--dump-schema', 'dump_schema')
options.add('--dump-migration', 'dump_migration')

options.execute()
