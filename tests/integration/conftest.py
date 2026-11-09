import pytest

from app.database import engine
from app.models.user import Base


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    """Create database tables before integration tests and clean up afterward."""
    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)
    