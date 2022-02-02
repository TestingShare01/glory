from django.test import TestCase

# Create your tests here.
from logzero import logger

logger.info("{:.0f}%".format(3/6*100))


