# coding:utf8

from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', borker='redis://localhost:6379/0')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
	
	# Calls test('hello') every 10s
	sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

	# Call test('world') every 30s
	sender.add_periodic_task(30.0, test.s('world'), expiress=10)

	# Exectes every MOnday morning at 7:30 am
	sender.add_periodic_task(
		crontab(hour=7, minute=30, day_of_week=1),
		test.s('Happy Monday')
	)


@app.task
def test(arg):
	print arg

