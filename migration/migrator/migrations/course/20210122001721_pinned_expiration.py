"""Migration for a given Submitty course database."""


def up(config, database, term, course):
    """
    Run up migration.

    :param config: Object holding configuration details about Submitty
    :type config: migrator.config.Config
    :param database: Object for interacting with given database for environment
    :type database: migrator.db.Database
    :param term: Semester of the course being migrated
    :type term: str
    :param course: Code of course being migrated
    :type course: str
    """
    if not database.table_has_column('threads', 'pinned_expiration'):
        database.execute("ALTER TABLE threads ADD IF NOT EXISTS pinned_expiration timestamp with time zone NOT null DEFAULT '1900-01-01 00:00:00'");
        database.execute("UPDATE threads SET pinned_expiration = CAST(CASE WHEN pinned = true THEN '9998-01-01 00:00:00' ELSE '1900-01-01 00:00:00' END AS timestamp with time zone)");
    pass


def down(config, database, term, course):
    """
    Run down migration (rollback).

    :param config: Object holding configuration details about Submitty
    :type config: migrator.config.Config
    :param database: Object for interacting with given database for environment
    :type database: migrator.db.Database
    :param term: Semester of the course being migrated
    :type term: str
    :param course: Code of course being migrated
    :type course: str
    """
    pass
