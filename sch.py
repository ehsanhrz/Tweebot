import schedule
import xxx
import main
import time
from apscheduler.schedulers.background import BackgroundScheduler

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(xxx.main,'cron',day_of_week = '0-6', hour = '23', minute = '45',timezone = 'Asia/Tehran')
    scheduler.add_job(main.telegram,'cron',day_of_week = '0-6', hour = '17', minute = '50,51,52,53,54,55,56',timezone = 'Asia/Tehran')
    scheduler.start()
