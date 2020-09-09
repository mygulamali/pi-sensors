# Pi-Sensors

## Setup

1. Install the Python packages: `pipenv install`


## Database migrations

We use [Alembic] to specify database migrations.

+ Create a new migration:
  ```
  pipenv run alembic revision -m "<MESSAGE>"
  ```
  where `MESSAGE` describes the migration.
+ To run all migrations:
  ```
  pipenv run alembic -x db_url=<DB_URL> upgrade head
  ```
  where `DB_URL` is of the format `driver://username:password@host:port/dbname`.
+ To rollback to the last migration:
  ```
  pipenv run alembic -x db_url=<DB_URL> downgrade -1
  ```

[Alembic]: https://alembic.sqlalchemy.org/ "Alembic"


## License

This software is released under the terms and conditions of [The MIT License].
Please see the `LICENSE` file for more details.

[The MIT License]: http://www.opensource.org/licenses/mit-license.php "The MIT License"
