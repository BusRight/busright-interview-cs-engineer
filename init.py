from mockfirestore import MockFirestore

def init_db():
  db = MockFirestore()
  return db