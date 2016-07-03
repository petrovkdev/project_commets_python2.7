# -*- coding: utf-8 -*-

#model page statistics
def page_stat(env, start_response, header, db, regionid = ''):
  start_response('200 OK', header)
  li = ''
  
  if regionid == '':
    sql = db.execute('select * from regions')
    regions = sql.fetchall()    
    
    for row in regions:
      sql = db.execute('select count() from comments where region = %d' % row[0])
      count = sql.fetchone()[0]
      if count > 5:
        li += '<li><a href="/stat/region/'+str(row[0])+'/"><b>'+row[1]+'</b></a>, комментариев: '+str(count)+'</li>'
    
    page = """
        <!DOCTYPE html>
        <html>
          <head>
            <title>Просмотр статистики</title>
            <meta charset="UTF-8">
          </head>
          <body>
            <h1>Меню</h1>
            <ul>
              <li><a href="/">На главную</a></li>
              <li><a href="/comment/">Добавление комментариев</a></li>
              <li><a href="/view/">Просмотр/удаление комментариев</a></li>
              <li><span>Просмотр статистики</span></li>
            </ul>
            <h1>Просмотр статистики</h1>
              <ul>"""+li+"""</ul>
          </body>
        </html>
      """
  else:
    sql = db.execute('select region from regions where id = %d' % regionid)
    region = sql.fetchone()[0]
    
    sql = db.execute('select * from city where region_id = %d' % regionid)
    cityall = sql.fetchall()
    
    for row in cityall:
      sql = db.execute('select count() from comments where city = %d group by region' % row[0])
      count = sql.fetchone()[0]
      li += '<li><b>'+row[1]+'</b>, комментариев: '+str(count)+'</li>'
      
    page = """
        <!DOCTYPE html>
        <html>
          <head>
            <title>Просмотр статистики</title>
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
            <h1>Просмотр статистики комментариев по региону: """+region+"""</h1>
              <ul>"""+li+"""</ul>
          </body>
        </html>
      """
    
  return page