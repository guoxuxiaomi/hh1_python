#encoding=utf-8
from fabric.api import run, env

env.hosts = '172.27.61.11:22'
env.user = 'root'
env.password = 'redhat'


def hello():
    print (env.hosts)
    out = run('ps -ef|grep tomcat')
    print(out)

hello()