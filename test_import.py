import sys
import traceback

try:
    import stbottle.wsgi
    print("Success")
except Exception as e:
    traceback.print_exc()
