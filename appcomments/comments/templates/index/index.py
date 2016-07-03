# -*- coding: utf-8 -*-

#model homepage
def page_index(env, start_response, header, db):

  start_response('200 OK', header)
  
  page = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Главная</title>
        <meta charset="UTF-8">
      </head>
      <body>
        <h1>Меню</h1>
        <ul>
          <li><span>На главную</span></li>
          <li><a href="/comment/">Добавление комментариев</a></li>
          <li><a href="/view/">Просмотр/удаление комментариев</a></li>
          <li><a href="/stat/">Просмотр статистики</a></li>
        </ul>
      </body>
    </html>
  """
  
  return page