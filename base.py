#!/usr/bin/python3
# -*- coding: utf-8 -*-

class StaticPage:
  '''A static page class.'''
      
  def __init__(self):
    self.title      = '''<title>DP</title>'''
    self.head       = '''<head></head>'''
    self.body       = '''<body></body>'''

  def ctitle(self, title):
    self.title = '''<title>{0}</title>'''.format(title)

  def chead(self, head):
    self.head = '''<head>{0}</head>'''.format(head)
  
  def cbody(self, body):
    self.body = '''<body><div>{0}</div></body>'''.format(body)
  
  def construct_page(self):
    return '<html>\n' + self.title + '\n' + self.head + '\n' + \
    self.body + '\n</html>'


class DinamicPage(StaticPage):
  def construct_page(self):
    return '<html>\n' + self.title + '\n' + self.head + '\n' + \
    self.body + '\n</html>'

    
if __name__=='__main__':
  page = StaticPage()
  print(page.construct_page())
  print('----')

  page.ctitle('New Title')
  page.chead('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
  page.cbody('<h1>Erst</h1>\nErnest Hemingway')
  with open('1.htm', 'w', encoding='utf8') as f:
    print(page.construct_page(), file=f)
    
  import webbrowser
  webbrowser.open('1.htm')
  
