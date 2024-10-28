class RadiantLandRouter:
    """
    A router to control all database operations on models in the
    land_management app, using MySQL and MSSQL databases.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read land_management models go to MySQL (default).
        """
        if model._meta.app_label == 'land_management':
            return 'default'  # MySQL
        return None  # Fallback to default database

    def db_for_write(self, model, **hints):
        """
        Attempts to write land_management models go to MySQL (default).
        """
        if model._meta.app_label == 'land_management':
            return 'default'  # MySQL
        return None  # Fallback to default database

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations only if both objects are from the same database.
        """
        if obj1._state.db == obj2._state.db:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the land_management app's models get created on the MySQL database.
        """
        if app_label == 'land_management':
            return db == 'default'  # MySQL
        return None
