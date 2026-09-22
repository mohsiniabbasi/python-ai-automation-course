import logging
logging.basicConfig(filename="shift.log",filemode='w', level=logging.WARNING, encoding='utf-8', format="%(asctime)s:%(levelname)s:%(message)s")
logging.info("Shift started")
logging.info("Job 1 finished, £14")
logging.debug("Checking tyre pressure")
logging.warning("Fuel level low")
logging.error("App crashed, job 2 lost")
logging.critical("Car broken down, shift ended")
