# -*- coding: utf-8 -*-
import time

#model page form add comments
def page_comment(env, start_response, header, db):
  start_response('200 OK', header)

  sql = db.execute("select * from regions")
  
  option = ''
  
  for row in sql:
    option += '<option value="'+str(row[0])+'">'+str(row[1])+'</option>'
      
  page = """
      <!DOCTYPE html>
      <html>
        <head>
          <title>Добавление комментариев</title>
          <meta charset="UTF-8">
          <link rel="stylesheet" href="/static/css"""+env['PATH_INFO']+"""main.css" type="text/css" media="all">
         </head>
        <body>
          <h1>Меню</h1>
          <ul>
            <li><a href="/">На главную</a></li>
            <li><span>Добавление комментариев</span></li>
            <li><a href="/view/">Просмотр/удаление комментариев</a></li>
            <li><a href="/stat/">Просмотр статистики</a></li>
          </ul>
          <h1>Добавление комментариев</h1>
          <form method="post" action="/comment/" id="form-comment">
            <div class="field require"><input type="text" class="control required" name="firstname" placeholder="Фамилия" id="firstname"></div>
            <div class="field require"><input type="text" class="control required" name="name" placeholder="Имя" id="name"></div>
            <div class="field"><input type="text" class="control" name="lastname" placeholder="Отчество" id="lastname"></div>
            <div class="field">
              <select class="control" name="region" id="region" onchange="changeRegion(this);">
                <option value="">Выбрать регион</option>"""+option+"""</select>
            </div>
            <div class="field">
              <select class="control" name="city" id="city" disabled>
                <option value="">Выбрать город</option>
              </select>
            </div>
            <div class="field">(<input type="text" class="control" maxlength="4" id="code" name="code" placeholder="код города">)<input class="control" maxlength="7" type="text" id="phone" name="phone" placeholder="Контактный телефон"></div>
            <div class="field"><input class="control" type="text" id="email" name="email" placeholder="E-mail"><div class="none incorrect">Некорректный e-mail</div></div>
            <div class="field require"><textarea class="control required" id="comment" name="comment" placeholder="Комментарий"></textarea></div>
            <p><input type="submit" value="Отправить" id="send" onclick="ajaxSubmit(); return false;"><i class="none" id="result"></i></p>
            
          </form>
          <script type="text/javascript" src="/static/js"""+env['PATH_INFO']+"""main.js"></script>
        </body>
      </html>
    """
  return page
  
#ajax change list select city
def ajax_city(env, start_response, header, db, post):
  start_response('200 OK', header)
  regionid = int(post.get('region',[''])[0])
  city = '<option value="">Выбрать город</option>'
  
  if regionid != '':
    sql = db.execute("select * from city where region_id = %d" % regionid)
    
    for row in sql:
      city += '<option value="'+str(row[0])+'">'+str(row[1])+'</option>'
    
  return city
  
#ajax addcomment
def ajax_comment(env, start_response, header, connectdb, db, post):
  start_response('200 OK', header)
  
  firstname = str(post.get('firstname',[''])[0])
  name      = str(post.get('name',[''])[0])
  lastname  = str(post.get('lastname',[''])[0])
  
  if post.get('region',[''])[0] == '':
    region = 0
  else:
    region    = int(post.get('region',[''])[0])
  
  if post.get('city',[''])[0] == '':
    city = 0
  else:
    city = int(post.get('city',[''])[0])
  
  if post.get('code',[''])[0] == '' and post.get('phone',[''])[0] == '':
    phone   = ''
  else:    
    phone   = '('+str(post.get('code',[''])[0])+')'+str(post.get('phone',[''])[0])  
  
  email     = str(post.get('email',[''])[0])
  comment   = str(post.get('comment',[''])[0])
  
  db.execute("INSERT INTO comments(first_name, name, last_name, region, city, phone, email, comment, timestamp) VALUES(?,?,?,?,?,?,?,?,?)", (firstname, name, lastname, region, city, phone, email, comment, int(time.time())))
  
  connectdb.commit()
  
  return 'Комментарий добавлен!'
  
  
  
  
  
  
  
  
