

# Поток событий
---

# Содержание
1 [Актёры](#actors)  
2 [Варианты использования](#use_case)  
2.1 [Синхронизировать время](#sync_time)  
2.2 [Добавить новое текстовое напоминание](#add_alert)  
2.3 [Добавить новое файловое напоминание](#add_file_alert)  
2.4 [Посмотреть все напоминания](#show_alert)  
2.5 [Редактировать напоминание](#edit_alert)  
2.6 [Отложить напоминание](#reset_alert)  
2.7 [Создать напоминание для другого человека](#external_alert)  
2.8 [Запретить принимать чужие напоминания](#cancel_external)  


<a name="actors"/>

# 1 Актёры

| Актёр | Описание |
|:--|:--|
| Новый пользователь | Человек, первый раз вошедший в систему |
| Пользователь | Человек, использующий систему |
| Сервер | Интернет ресурс для получения часового пояса  |
| База | База данных, хранящая напоминания пользователей  |

<a name="use_case"/>

# 2 Варианты использования

Use Case диаграммы приложения "# MegaReminder бот для Telegram":
![Диалог добавления напоминания](../../Images/System design/use.png) 



<a name="sync_time"/>

## 2.1 Синхронизировать время
(https://astrology.pro/timezoneandplace/)
**Описание.** Вариант использования "Синхронизировать время" позволяет пользователю настроить часовой пояс сервера и получать напоминания вовремя.  

**Основной поток.**
1. Вариант использования начинается, когда пользователь первый раз запускает бота.
2. Приложение предлагает пользователю ввести его город. 
3. Пользователь вводит свой город;
4. Приложение выполняет запрос на интернет-ресурс и получает часовой пояс пользователя.
5. Конец варианта использования. 

<a name="add_alert"/>

## 2.2 Добавить новое текстовое напоминание

**Описание.** Вариант использования "Добавить новое текстовое напоминание" позволяет пользователю создать новое напоминание в виде текста.  
**Предусловия.** Пользователь уже прошел вариант  использования "Синхронизировать время".  
1. Пользователь оправляет боту сообщение, содержащее текст напоминания и временную метку.
2. Бот проверяет данные на наличие ошибок и, в случае их отсутствия, переходит к пункту 5.
3. При наличии ошибок бот прост пользователя повторить либо ввод данных либо ввод времени.
4. Бот выполняет пункт 2.
5. Бот сохраняет новое напоминание в базе.
6. Конец варианта использования. 


<a name="show_alert"/>

## 2.3 Добавить новое файловое напоминание

**Описание.** Вариант использования "Добавить новое файловое напоминание" позволяет пользователю создать новое напоминание в виде фотографии, или другого медиа, поддерживемого Telegram.
**Предусловия.** Пользователь уже прошел вариант  использования "Синхронизировать время".  
1. Пользователь оправляет боту сообщение, содержащее фотографию, или другое медиа.
2. Бот просить пользователя отправить ему временную метку.
3. Бот проверяет данные на наличие ошибок и, в случае их отсутствия, переходит к пункту 6.
4. При наличии ошибок бот прост пользователя повторить отправку временной метки.
5. Бот выполняет пункт 2.
6. Бот сохраняет новое напоминание в базе.
7. Конец варианта использования. 


<a name="show_alert"/>

## 2.4 Посмотреть все напоминания
 **Описание.** Вариант использования "Посмотреть все напоминания" позволяет пользователю получить список всех добавленных напоминаний.
1. Пользователь отправляет боту сообщенные, содержащее временную метку того дня, все напоминания книготорг необходимо вывести.
2. В случае отсутствия ошибок, бот паре ходит к пунктику 5.
3. Бот просит пользователя повторить отправку временной метки.
4. Бот отправляет пользователю список всех напоминаний относящихся к переданной метке.
5. Конец варианта использования. 



<a name="edit_alert"/>

## 2.5 Редактировать напоминание

**Описание.** Вариант использования "Редактировать напоминание" позволяет пользователю изменить либо текст либо время напоминания.  
1. Пользователь выполняет вариант использования "Посмотреть все напоминания".
2. Пользователь отправляет номер напоминания, которое необходимо изменить.
3. Пользователь отправляет новое напоминание или временную метку.
4. Бот сохраняет изменения в базе напоминаний.
5. Конец варианта использования. 


<a name="reset_alert"/>

## 2.6 Отложить напоминание

**Описание.** Вариант использования "Отложить напоминание" позволяет пользователю повторить напоминание через указанный промежуток времени.  
1. Бот присылает пользователю напоминание в виде входящего сообщения.
2. Пользователь отвечает на него временной меткой, обозначающей время, когда необходимо повтрить напоминание.
3. Бот сохранят изменения в базе.
4. Конец варианта использования. 


<a name="external_alert"/>

## 2.7 Создать напоминание для другого человека

**Описание.** Вариант использования "Создать напоминание для другого человека" позволяет пользователю послать напоминание другому человеку.  
1. Пользователь выполняет вариант использования "Посмотреть все напоминания".
2. Пользователь отправляет номер человеку, кому необходимо переадресовать напоминание.
3. Бот сохраняет изменения в базе. 
4. Конец варианта использования. 


<a name="cancel_external"/>

## 2.8 Запретить принимать чужие напоминания

**Описание.** Вариант использования "Запретить принимать чужие напоминания" позволяет пользователю запретить принимать чужие напоминания.  

1. Для отмены или разрешения чужих напоминаний пользователь отправляет боту сообщение с текстом "разрешить/запретить принимать чужие напоминания".
2. Бот сохраняет изменения в базе. 
3. Конец варианта использования. 