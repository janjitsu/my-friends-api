server:
	uvicorn app.main:app --port 8000 --host 0.0.0.0 --reload

test:
	pytest

build:
	docker image build -t my-friends-api .

container:
	docker container run -p 8000:8000 my-friends-api
