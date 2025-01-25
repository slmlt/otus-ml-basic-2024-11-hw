from homework_06.base import Vehicle
from homework_06.engine import Engine


class Car(Vehicle):
    engine: Engine

    def set_engine(self, engine: Engine):
        self.engine = engine
