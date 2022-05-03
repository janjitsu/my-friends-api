server:
	uvicorn app.main:app --reload

test:
	pytest
