import logging
import sys
# the default log level is WARNING in logging module

# initialize :
logger = logging.getLogger(__name__)

# using basicConfig to set the logger : 
logging.basicConfig(level = logging.INFO, filename = 'calculator.log', format = "%(asctime)s %(levelname)s - %(message)s")

# If adding an streamer :   -> the meassage will show in the console 
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

def division():
  logger.debug("Starting Division!")
  try:
    dividend = float(input("Enter the dividend: "))
    logger.info(dividend)
    divisor = float(input("Enter the divisor: "))
    logger.info(divisor)
  except SyntaxError:
    logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
    return
  if divisor == 0:
    logger.error("Attempting to divide by 0!")
    return
  else:
      return dividend/divisor

result = division()
if result == None:
  logger.warning("The result value is None!")