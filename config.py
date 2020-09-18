# 我是配置文件
CSRF_ENABLED = True
SECRET_KEY = '***********************************'

OPENID_PROVIDERS = [
    {'name': 'Google','url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo','url': 'https://me.yahoo.com'},
    {'name': 'AOL','url': 'http://openid.aol.com/<username>'},
    {'name': 'Baidu','url': 'http://www.baidu.com/<username>'},
    {'name': 'MyOpenID','url': 'https://www.myopenid.com'},
]