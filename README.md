# DermaCenter2
Dermacenter practice part 2

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
python -m pip install --user virtualenv
python -m venv env

.\env\Scripts\activate
source env/Scripts/Activate

docker-compose up --build

docker run --rm -it -p 8000:8000  python-test

$${POSTGRES_DB}

python -m pip install -r requirements.txt