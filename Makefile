run:
	uvicorn main:app --app-dir src  --host 0.0.0.0 --port 8088 --reload

install-dep:
	pip install -r src/requirements.txt