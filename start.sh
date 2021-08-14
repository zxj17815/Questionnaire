cd /root/python/Questionnaire
source /root/python/Questionnaire/venv/bin/activate
exec /root/python/Questionnaire/venv/bin/gunicorn main:app -c /root/python/Questionnaire/gunicorn.py