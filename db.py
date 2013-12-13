
class Db:
	def __init__(self):
		pass

	def connect(self, options):
		if options.db_type == 'sqlite':
			try:
				import sqlite3 as dbmodule
			except ImportError:
				raise ValueError('Cannot open an sqlite database without sqlite3 python module')

			self.connection = dbmodule.connect(options.db_name)
		elif options.db_type == 'postgres':
			try:
				import psycopg2 as dbmodule
			except ImportError:
				raise ValueError('Cannot connect to a postgres database without psycopg2 installed')

			self.connection = dbmodule.connect(database=options.db_name,
			                                   user=options.db_user,
			                                   password=options.db_password,
			                                   host=options.db_host)
		else:
			raise ValueError('Invalid database type: %s' % (options.db_type))

		cursor = self.connection.cursor()
		return cursor
