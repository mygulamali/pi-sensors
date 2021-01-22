.PHONY: serve
serve:
	pipenv run uvicorn --reload --reload-dir app --app-dir app main:app

.PHONY: setup
setup:
	pipenv install --dev
	cp ansible/hosts.example.yml ansible/hosts.yml

.PHONY: deploy
deploy:
	pipenv run ansible-playbook -i ansible/hosts.yml ansible/deploy.yml
