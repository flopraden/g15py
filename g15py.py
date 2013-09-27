#Interact with the g15 LCD screen using python on Windows!

from ctypes import *
import time

def _warning(f):
    '''
    Tell people to put the dll in the folder.
    '''
    def inner(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except WindowsError as e:
            if e.args == (126, 'The specified module could not be found'):
                raise WindowsError('LogitechLcd.dll (found in the sdk) needs to be put in the same folder as the g15py.py module')
            raise e
    return inner

@_warning
def init(name='Python Script'):
    cdll.LogitechLcd.LogiLcdInit(c_wchar_p(name), c_int(1))

@_warning
def set_text(text, line=0):
    cdll.LogitechLcd.LogiLcdMonoSetText(c_int(line), c_wchar_p(text));
    cdll.LogitechLcd.LogiLcdUpdate()

@_warning
def shutdown():
    cdll.LogitechLcd.LogiLcdShutdown()


if __name__ == '__main__':
    try:
        init('Name of script')
        set_text('Sample text', line=0)
        set_text('More text', line=1)
        time.sleep(3)
    finally:
        shutdown()
