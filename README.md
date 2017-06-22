# channelsui
## readme

    mkdir /var/www/channelsui
    cd /var/www/channelsui
    git clone https://github.com/nsushkov/channelsui


Скопировать файлы shortestpath.py  и  qcrypt.py 
в дирректорию ...ryu/app

### Что необходимо установить для работы:

Т к, Python 2.7 уже присутствует, необходим только Django v 1.11>
в девелоперской версии продукта достаточно простого отладочного сервера в составе фреймворка Django, который будет запускаться.
В дальнейшем понадобится Nginx.

Необходимо  открыть порт, на котором будет запускаться сервер django - по умолчанию 8000

### Порядок запуска:

После запуска naulinux c mininet и ryu на борту запустить Django сервер:

 cd ---
 python manage.py runserver servipaddr

где servipaddr - адрес в локальной сети машины, на которой запускается сервер
