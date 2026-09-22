import logging
logging.basicConfig(filename="taxi.log",level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

logging.debug("Checking sat nav")
logging.info("Job started: Leeds station")
#logging.warning("Fare missing on job 7")
logging.error("Payment failed")
#logging.critical("Car broken down")