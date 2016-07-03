# -*- coding: utf-8 -*-

#model page 404
def page404(env, start_response, header):
  start_response('404', header)
  page = """<!DOCTYPE html>
    <html>
      <head>
        <title>404</title>
        <meta charset="UTF-8">
      </head>
      <body>
        <h1>Меню</h1>
        <ul>
          <li><a href="/">На главную</a></li>
          <li><a href="/comment/">Добавление комментариев</a></li>
          <li><a href="/view/">Просмотр/удаление комментариев</a></li>
          <li><a href="/stat/">Просмотр статистики</a></li>
        </ul>
        <h1>404</h1>
      </body>
    </html>
    """
  return page