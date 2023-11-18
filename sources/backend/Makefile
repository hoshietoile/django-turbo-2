dev:
	poetry install && \
	# poetry run python /workspaces/django_turbo/sources/backend/app/manage.py migrate && \
	poetry run python /workspaces/django_turbo/sources/backend/app/manage.py spectacular --file schema.yaml && \
	poetry run python /workspaces/django_turbo/sources/backend/app/manage.py runserver 0.0.0.0:8000

generate-types:
	poetry install && poetry run python /workspaces/django_turbo/sources/backend/app/manage.py spectacular --file schema.yaml