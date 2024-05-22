export FLASK_APP=core/server.py
rm instance/store.sqlite3
# rm core/store.sqlite3
flask db upgrade -d core/migrations/

pytest -vvv -s tests/

# pytest --cov
coverage html
open htmlcov/index.html