import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
login = os.getenv("LOGIN")
login = os.getenv("PASSWORD")
my_str = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
my_str= my_str.replace('%website%',"https://dvmn.org/referrals/cKHsKjCwFJ2huOZkBILdnm3osBAMhU40ZgaK0ypx/")
my_str= my_str.replace('%friend_name%',"Александр")
my_str= my_str.replace('%my_name%',"Никита")
From ="devmanorg@yandex.ru"
To ="nikitadevman@yandex.ru"
Subject ="Приглашение!"
Content_type = "text/plain; charset='UFT-8'"
charset='UFT-8'
letter = """From:{0},{1},{2},{3},{4}""".format(From,To,Subject,Content_type,  my_str)
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login('devmanorg@yandex.ru' , 'jdaewfpbrtiacmvf')
server.sendmail('devmanorg@yandex.ru', 'nikitadevman@yandex.ru', my_str.encode('utf-8')) 
server.quit()










