.PHONY: init_venv deps freeze clean_venv

all: init_venv deps database superuser
	PYTHONPATH=venv ; venv/bin/activate

init_venv:
	if [ ! -e "venv/bin/activate_this.py" ] ; then PYTHONPATH=venv ; python3.6 -m venv venv; fi

deps:
	PYTHONPATH=venv ; . venv/bin/activate && venv/bin/pip install -U -r requirements.txt && if [ "$(ls requirements)" ] ; then venv/bin/pip install -U -r requirements/* ; fi

freeze:
	venv/bin/activate && venv/bin/pip freeze > requirements.txt

database:
	venv/bin/activate && venv/bin/python manage.py makemigrations user common cases emails accounts contacts opportunity leads && venv/bin/python manage.py migrate

collectstatic:
	venv/bin/activate && venv/bin/python manage.py collectstatic

superuser:
	venv/bin/activate && venv/bin/python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@THcrm.com', 'techhell')"

clean_venv:
	rm -rf venv

reset_db:
	mv db.sqlite3 db.sqlite3_old ;
	rm -rf user/migrations common/migrations cases/migrations emails/migrations accounts/migrations contacts/migrations opportunity/migrations leads/migrations
