initialize_git:
	@echo "git initialization"
	git init 
	sleep 1
	git add .
	sleep 1
	git commit -m "first commit"
	sleep 1
	git branch -M main
	sleep 1
	git remote add origin origin https://github.com/EDJINEDJA/ChatDoctor-DB.git
	sleep 1
	git push -u origin main

env:
	@echo "env configuration ..."
	pipenv run pre-commit install

pip_git:
	@echo "pushing ..."
	git add .
	git commit -m $(var)
	git push -u origin main

pul_git:
	@echo "pulling ..."
	git pull origin main

run:
	python app.py

config: initialize_git env
	
