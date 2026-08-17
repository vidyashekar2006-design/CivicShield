import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


# Load variables from the project's .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not configured. "
        "Please check the .env file."
    )


# Create a reusable SQLAlchemy engine.
# pool_pre_ping helps detect stale database connections.
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True,
)


def test_connection() -> None:
    """Verify the CivicPulse PostgreSQL connection."""

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), version();")
        )

        database_name, version = result.fetchone()

        print("Database connection successful.")
        print(f"Database: {database_name}")
        print(f"PostgreSQL: {version}")


if __name__ == "__main__":
    test_connection()