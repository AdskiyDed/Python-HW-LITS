import logging

from div1 import d

fmt= '%(asctime)s : %(name)s : %(levelname)s - %(message)s'

logging.basicConfig(
    filename='log.log',
    filemode='w',
    level=logging.DEBUG,
    format=fmt
)
logging.debug('start function d')
print(d(10,2))
logging.debug('done')
