from django.db import connection
from django.http import JsonResponse

def dapau(request):
    raise Exception("break on purpose")



def status(request):
    cursor = connection.cursor()
    cursor.execute("""SELECT 1+1""")
    row = cursor.fetchone()
    return JsonResponse({"status": "ok", "db": "ok" if row == (2,) else "error"})



