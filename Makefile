.PHONY: serve
serve:
	pipenv run uvicorn --reload --reload-dir app --app-dir app main:app

.PHONY: setup
setup:
	pipenv install --dev
	cp hosts.example.yml hosts.yml

.PHONY: deploy
deploy:
	pipenv lock -r > requirements.txt
	pipenv run ansible-playbook -i hosts.yml deploy.yml
	rm requirements.txt
