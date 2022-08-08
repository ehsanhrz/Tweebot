import schedule
import xxx
import main
import time


def algho():

    
    schedule.every().day.at("23:45").do(xxx.main)
    # schedule.every(2).minutes.do(main.telegram)
    schedule.every(3).hour.at("11:30").to("23:30").do(main.telegram)
    
    while True:
        schedule.run_pending()
        time.sleep(1)