#!/usr/bin/python3
"""Lists all State objects that contain the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name = "Louisiana")
    session.add(new_state)
    instance = session.query(State).filter(State.name == "%s" % (new_state.name, )).first()
    print(instance.id)
