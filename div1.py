import logging

logger = logging.getLogger('div1')

def d(a,b):
    # logging.debug('started function d')
    try:
        c = a / b
        logging.debug(c)
        return c
    except ArithmeticError as e:
        logging.exception ('b is zero',
        # exc_info=True
                           )