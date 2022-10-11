from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

# from lib.loaders import load_models

# Export just the db and init_db symbols when 'from db import *' is used
__all__ = ('db', 'init_db')   

# our global DB ojbect (imported by models and views)
db = SQLAlchemy()

# support importing a functioning session query
query = db.session.query

def init_db(app=None, db=None):
   """Initializes the global database object used by the app."""
   if isinstance(app, Flask) and isinstance(db, SQLAlchemy):
      # force_auto_coercion()
      # load_models()
      db.init_app(app)
      
   else:
      raise ValueError('Cannot init DB without db and app objects.')