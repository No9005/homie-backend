requirements:
	poetry lock --no-update
	poetry export --without-hashes > requirements.txt
	poetry export --with dev --without-hashes > requirements-dev.txt