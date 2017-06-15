# Makefile for managing GitHub Classroom

.PHONY: venv
venv:
	python3 -m venv _venv
	source _venv/bin/activate
	pip install -r requirements.txt

.PHONY: run
run:
	python3 app.py

