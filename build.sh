#Install dependencies
pip3 install -r deps.txt

python manage.py collectstatic --no-input
#Run migrations
python3 manage.py migrate