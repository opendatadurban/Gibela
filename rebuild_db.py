from gibela.models import db
from gibela.models.seeds import seed_db

db.drop_all()
db.create_all()
seed_db(db)
