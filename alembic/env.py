from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from app.models.postgres.base import BaseModelORM
from app.models.postgres import *
from app.models.postgres.influencer import Influencer
from app.models.postgres import user 


# Alembic config object
config = context.config

# Carrega logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define o metadata dos modelos
target_metadata = BaseModelORM.metadata

# MIGRAÇÕES OFFLINE
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# MIGRAÇÕES ONLINE
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # detecta alterações de tipo
        )
        with context.begin_transaction():
            context.run_migrations()

# Decide qual modo rodar
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
