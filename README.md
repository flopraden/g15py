g15py
=====

Interact with the g15 LCD screen using python on Windows!


###Usage
```
from g15py import init, set_text, shutdown
import time

try:
    init('Name of script')
    set_text('Sample text', line=0)
    set_text('More text', line=1)
	time.sleep(3)
finally:
    shutdown()
```
