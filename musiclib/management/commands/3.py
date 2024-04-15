import subprocess
from django.core.management import BaseCommand

from musiclib.models import CustomUser, MusicFiles


class Command(BaseCommand):

    def handle(self, *args, **options):
    
        # SipHeader()
        # from django.conf import settings
        # document_root=settings.STATIC_ROOT
        queryset = MusicFiles.objects.all().filter(customuser=6)
        print(queryset)
        # subprocess.run(f"sed 's/>\{queryset}<\/\option>\/>\{queryset}<\/\option>\\n <p>{queryset}</p>/i' antrading/templates/antrading/antrading_home.html>file_out && mv antrading/templates/antrading/antrading_home.html", shell=True)
        # subprocess.run("sed 's/EMAIL_USE_TLS = False/EMAIL_USE_TLS = True/i' config/settings.py>file_out && mv file_out config/settings.py ", shell=True)
        # subprocess.run("sed 's/</\select>\/i your text 1nyour text 2nyour text 3/i' antrading/templates/antrading/antrading_home.html>file_out && mv file_out antrading/templates/antrading/antrading_home.html ", shell=True)
        # dupl(['a','d','g', 'a', 'd'])
        # get_variants([((1,2,3),(4,5,6))])
#Общий пример создания потоков классом Thread.
# import threading


# def worker(i):
#     """thread worker function"""
#     print(f'Worker-{i}')


# threads = []
# # запускаем функцию 'worker()' 
# # для выполнения в 5-ти потоках
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()
    
# # блокируем дальнейшее выполнение программы
# # пока не закончат выполняться все 5 потоков
# [thread.join() for thread in threads]