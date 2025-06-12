from waitress import serve
from cmsimde import flaskapp

serve(flaskapp.app, listen='2001:288:6004:17:fff1:cd25:0:a056', threads=8)
