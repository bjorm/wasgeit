#!/var/www/cgi-bin/python3-wasgeit/bin/python3
from flipflop import WSGIServer
from backend import app

if __name__ == '__main__':
    WSGIServer(app).run()
