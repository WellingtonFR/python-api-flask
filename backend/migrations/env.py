from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from app.models import db
import os

config = context.config
target_metadata = db.metadata

def run_migrations_offline():
    pass

def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section),
                                     prefix='sqlalchemy.',
                                     poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
