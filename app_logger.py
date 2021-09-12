import logging
import os

# # Logs directory
# logs_dir = "logfiles"
# logfile_name = "video_logs"

# # Define logger object, add formatters and handlers
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# file_handler = logging.FileHandler(os.path.join(logs_dir,logfile_name))
# formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

def app_logger(logfile_name, log_level,dest=None,logs_dir="logfiles",
 log_format = "%(asctime)s : %(levelname)s : %(name)s : %(message)s"):

	"""
	Function to return a logger object. 
	Required to add logfile_name and log_level fields.

	logfile_name -> name of file where logs are to be stored.
	log_level -> logging level to be set.
	dest -> namespace to be used. Use __name__ 
	log_dir -> parent directory for the logfiles. 
	"""

	if dest is not None:
	# Define logger object 
		logger = logging.getLogger(dest)

	# add formatters and handlers
	levels = ["DEBUG","INFO","WARNING","ERROR","CRITICAL"]

	if log_level.upper() in levels:
		logger.setLevel(log_level)
	else:
		print(f"Incorrect level provided. It should be one of {levels}")

	file_handler = logging.FileHandler(os.path.join(logs_dir,logfile_name))
	formatter = logging.Formatter(log_format)

	# set formatters and handlers
	file_handler.setFormatter(formatter)
	logger.addHandler(file_handler)
		
	return logger




