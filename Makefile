.PHONY: serve
serve:
	pipenv run uvicorn --reload --reload-dir app --app-dir app main:app

.PHONY: init
init:
	pipenv install --dev
	pipenv run pre-commit install
	cp ansible/hosts.example.yml ansible/hosts.yml

.PHONY: setup
setup:
	ANSIBLE_NOCOWS=1 pipenv run ansible-playbook -i ansible/hosts.yml ansible/setup.yml

.PHONY: deploy
deploy:
	ANSIBLE_NOCOWS=1 pipenv run ansible-playbook -i ansible/hosts.yml ansible/deploy.yml
