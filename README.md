# Migrate

This is a work in progress.

But the basic idea is to allow for simple database migrations that are framework agnostic. After all it's just string manipultion, right?

It should be as simple as this...

```python
import migrate

class CreateUsers(migrate.Migration):
  def up():
    self.create_table('users')
    self.string('full_name')
    self.string('email')
  def down():
    self.drop_table('users')

```

And just as simple to apply migrations, rollback and work with the data...

```bash
python migrate.py --init
python migrate.py --create_migration create_users
python migrate.py --migrate
python migrate.py --rollback --steps 2
python migrate.py --load-schema
python migrate.py --dump-schema
python migrate.py --dump-sql --migration create_users
python migrate.py --dump-sql --all
```
