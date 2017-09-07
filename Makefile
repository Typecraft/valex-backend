
.PHONY: run
run:
	python manage.py runserver 0.0.0.0:8010

.PHONY: test
test:
	python manage.py test

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: makemigr
makemigr:
	python manage.py makemigrations


.PHONY: freeze
freeze:
	rm -f requirements.txt && pip freeze > requirements.txt
