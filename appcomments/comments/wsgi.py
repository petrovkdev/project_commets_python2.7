# -*- coding: utf-8 -*-
import os
import sys
import re
import sqlite3 as db
from cgi import parse_qs
sys.path.append('templates/index')
sys.path.append('templates/comment')
sys.path.append('templates/view')
sys.path.append('templates/stat')
sys.path.append('templates/404')
import index 
import comment
import view
import pagestat
import page404

# connect db
con = db.connect('testdb.db')
con.text_factory = str
cur = con.cursor()

#common controller
def application(env, start_response):
  #header page
  head = [('Content-Type','text/html')]
  
  try:
    content_length = int(env.get('CONTENT_LENGTH', 0))
  except (ValueError):
    content_length = 0
    
  #read post data content_length
  req = env['wsgi.input'].read(content_length)
  
  #parse post data and get array post
  post = parse_qs(req)
  
  # action homepage
  if env['PATH_INFO'] == '/': 
    html = index.page_index(env, start_response, head, cur)
    
  # action comment page (form addcomment)
  elif env['PATH_INFO'] == '/comment/':    
    if post.get('ajax',[''])[0] == 'Y':
      if post.get('action',[''])[0] == 'rchange':        
        html = comment.ajax_city(env, start_response, head, cur, post)
      if post.get('action',[''])[0] == 'addcomment':
        html = comment.ajax_comment(env, start_response, head, con, cur, post)
    else:    
      html = comment.page_comment(env, start_response, head, cur)
      
  #page view comments
  elif env['PATH_INFO'] == '/view/':   
    if post.get('ajax',[''])[0] == 'Y':
      if post.get('action',[''])[0] == 'delcomment':        
        html = view.ajax_delete_comment(env, start_response, head, con, cur, post)
    else:
      html = view.page_view(env, start_response, head, cur)
  
  #page, number of reviews by region
  elif env['PATH_INFO'] == '/stat/':
    html = pagestat.page_stat(env, start_response, head, cur)
  
  #page, the number of comments on the cities of the region
  elif re.search(r'/stat/region/\d/$', env['PATH_INFO']):    
    idregion = re.findall(r'\d',env['PATH_INFO'])
    html = pagestat.page_stat(env, start_response, head, cur, int(idregion[0]))
  
  #page 404
  else:
    html = page404.page404(env, start_response, head)

  #release html template
  return html