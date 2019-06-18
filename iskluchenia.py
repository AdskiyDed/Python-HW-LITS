n = 2
try:
    print(2 / n)
except Exception as err:
    print(f'error type {err}', err)
# except:

else:
    print('done!')
finally:
    print('final print')
