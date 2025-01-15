from sqlalchemy.orm import Session, sessionmaker

from domain.unit_of_work import UnitOfWork


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory
        self._session: Session | None = None

    def __enter__(self):
        self._session = self.session_factory()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self._session.close()

    def commit(self):
        if self._session:
            self._session.commit()

    def rollback(self):
        if self._session:
            self._session.rollback()

    def session(self) -> Session:
        if not self._session:
            raise RuntimeError("Unit of Work has no active session.")
        return self._session
