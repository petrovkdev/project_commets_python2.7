# -*- coding: utf-8 -*-
import time

#model view commentarios
def page_view(env, start_response, head, db):
  start_response('200 OK', head)
  
  sql = db.execute('select c.id, c.first_name, c.name, c.last_name, r.region region, g.city city, c.phone, c.email, c.comment, c.timestamp from comments c LEFT JOIN regions r ON c.region = r.id LEFT JOIN city g ON c.city = g.id')
  
  comments = sql.fetchall()
  
  tr = ''
  
  for row in comments:
    date = time.strftime('%d.%m.%Y',time.gmtime(row[9]))
    tr += '<tr id="comment-'+str(row[0])+'" class="row"><td>'+row[1]+'</td><td>'+row[2]+'</td><td>'+row[3]+'</td><td>'+row[4]+'</td><td>'+row[5]+'</td><td>'+row[6]+'</td><td>'+row[7]+'</td> <td>'+row[8]+'</td><td>'+date+'</td><td><button type="button" onclick="delComment(this);" data-id="comment-'+str(row[0])+'">Удалить</button></td></tr>'

    page = """
      <!DOCTYPE html>
      <html>
        <head>
          <title>Просмотр/удаление комментариев</title>
          <meta charset="UTF-8">
          <link rel="stylesheet" href="/static/css"""+env['PATH_INFO']+"""main.css" type="text/css" media="all">
        </head>
        <body>
          <h1>Меню</h1>
          <ul>
            <li><a href="/">На главную</a></li>
            <li><a href="/comment/">Добавление комментариев</a></li>
            <li><span>Просмотр/удаление комментариев<span></li>
            <li><a href="/stat/">Просмотр статистики</a></li>
          </ul>
          <h1>Просмотр/удаление комментариев</h1>
          <div class="none" id="result">Комментарий удален!</div>
          <div id="content">"""
          
  if tr == '':
    page += """<h3>Нет комментариев для просмотра!<h3>"""
  else:
    page += """<table id="list_comment">
              <tr>
                <th>Фамилия</th>
                <th>Имя</th>
                <th>Отчество</th>
                <th>Регион</th>
                <th>Город</th>
                <th>Контактный телефон</th>
                <th>E-mail</th>
                <th>Комметарий</th>
                <th>Дата</th>
                <th>Действие</th>
              </tr>
              """+tr+"""
            </table>"""            
            
    page += """</div>
          <script type="text/javascript" src="/static/js"""+env['PATH_INFO']+"""main.js"></script>
        </body>
      </html>
    """
  return page

#ajax delete comment
def ajax_delete_comment(env, start_response, head, connectdb, db, post):
  start_response('200 OK', head)
  db.execute('delete from comments where id = %d' % int(post.get('id',[''])[0]))
  connectdb.commit()
  return false