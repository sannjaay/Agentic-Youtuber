from apscheduler.schedulers.blocking import BlockingScheduler
from graph import run_graph

scheduler = BlockingScheduler()

scheduler.add_job(run_graph, "cron", hour=18, minute=0)

scheduler.start()
