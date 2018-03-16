#encoding=utf-8
import paramiko
import sys,os

def upload(host):
    t = paramiko.Transport((host, 22))
    t.connect(username='root', password='redhat')
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put('D:\\workspace\\caizidao\\czd-server\\target\\czd-server.war',
             '/opt/apache-tomcat-7.0.76/webapps/czd-server.war')
    sftp.close()
    t.close()

def upload_pro(host):
    t = paramiko.Transport((host, 22))
    t.connect(username='root', password='redhat')
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put('D:\\workspace\\caizidao\\czd-server\\target\\czd-server.war',
             '/opt/apache-tomcat-8.0.26/webapps/czd-server.war')
    sftp.close()
    t.close()

def upload_zk():
    t = paramiko.Transport(('172.27.62.11', 22))
    t.connect(username='root', password='redhat')
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get('/opt/apache-tomcat-8.0.26/webapps/czd_share.tar.gz','D:\\workspace\\caizidao\\czd-server\\target\\czd_share.tar.gz')
    sftp.close()
    t.close()
    t2 = paramiko.Transport(('172.27.62.21', 22))
    t2.connect(username='root', password='redhat')
    sftp2 = paramiko.SFTPClient.from_transport(t2)
    sftp2.put('D:\\workspace\\caizidao\\czd-server\\target\\czd_share.tar.gz','/opt/apache-tomcat-8.0.26/webapps/czd_share.tar.gz')
    sftp2.close()
    t2.close()
    t3 = paramiko.Transport(('172.27.61.11', 22))
    t3.connect(username='root', password='redhat')
    sftp3 = paramiko.SFTPClient.from_transport(t3)
    sftp3.put('D:\\workspace\\caizidao\\czd-server\\target\\czd_share.tar.gz','/opt/apache-tomcat-7.0.76/webapps/czd_share.tar.gz')
    sftp3.close()
    t3.close()
    t4 = paramiko.Transport(('172.27.61.51', 22))
    t4.connect(username='root', password='redhat')
    sftp4 = paramiko.SFTPClient.from_transport(t4)
    sftp4.put('D:\\workspace\\caizidao\\czd-server\\target\\czd_share.tar.gz','/opt/apache-tomcat-7.0.76/webapps/czd_share.tar.gz')
    sftp4.close()
    t4.close()

def command_linux(command):
    host = '172.27.61.11'
    user = 'root'
    password = 'redhat'
    port = 22
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, user, password, timeout=5)
    stdin, stdout, stderr = ssh.exec_command(command)
    cmd_result = stdout.read(), stderr.read()
    ssh.close()
    return str(cmd_result[0],encoding= "utf8")

def command_linux_second(command):
    host = '172.27.61.51'
    user = 'root'
    password = 'redhat'
    port = 22
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, user, password, timeout=5)
    stdin, stdout, stderr = ssh.exec_command(command)
    cmd_result = stdout.read(), stderr.read()
    ssh.close()
    return str(cmd_result[0],encoding= "utf8")

def command_linux_pro(command):
    host = '172.27.62.11'
    user = 'root'
    password = 'redhat'
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, user, password, timeout=5)
    stdin, stdout, stderr = ssh.exec_command(command)
    cmd_result = stdout.read(), stderr.read()
    ssh.close()
    return str(cmd_result[0],encoding= "utf8")

def command_linux_pro_second(command):
    host = '172.27.62.21'
    user = 'root'
    password = 'redhat'
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, user, password, timeout=5)
    stdin, stdout, stderr = ssh.exec_command(command)
    cmd_result = stdout.read(), stderr.read()
    ssh.close()
    return str(cmd_result[0],encoding= "utf8")

# upload_zk();
cmd_result = ''
cmd_result_last = ''
upload(host = '172.27.61.11')
cmd_result = command_linux('pgrep -f tomcat')
cmd_result = command_linux('kill -9 '+cmd_result)
cmd_result = command_linux('rm -rf /opt/apache-tomcat-7.0.76/webapps/czd-server')
cmd_result = command_linux("bash -l -c '/opt/apache-tomcat-7.0.76/bin/startup.sh';cd /opt/apache-tomcat-7.0.76/webapps/;tar -xvzPf czd_share.tar.gz czd_share")

upload_pro(host='172.27.62.11')
cmd_result = command_linux_pro('pgrep -f tomcat')
cmd_result = command_linux_pro('kill -9 '+cmd_result)
cmd_result = command_linux_pro('rm -rf /opt/apache-tomcat-8.0.26/webapps/czd-server')
cmd_result = command_linux_pro("bash -l -c '/opt/apache-tomcat-8.0.26/bin/startup.sh';cd /opt/apache-tomcat-8.0.26/webapps/;tar -xvzPf czd_share.tar.gz czd_share")

upload_pro(host='172.27.62.21')
cmd_result = command_linux_pro_second('pgrep -f tomcat')
cmd_result = command_linux_pro_second('kill -9 '+cmd_result)
cmd_result = command_linux_pro_second('rm -rf /opt/apache-tomcat-8.0.26/webapps/czd-server')
cmd_result = command_linux_pro_second("bash -l -c '/opt/apache-tomcat-8.0.26/bin/startup.sh';cd /opt/apache-tomcat-8.0.26/webapps/;tar -xvzPf czd_share.tar.gz czd_share")

upload(host = '172.27.61.51')
cmd_result = command_linux_second('pgrep -f tomcat')
cmd_result = command_linux_second('kill -9 '+cmd_result)
cmd_result = command_linux_second('rm -rf /opt/apache-tomcat-7.0.76/webapps/czd-server')
cmd_result = command_linux_second("bash -l -c '/opt/apache-tomcat-7.0.76/bin/startup.sh';cd /opt/apache-tomcat-7.0.76/webapps/;tar -xvzPf czd_share.tar.gz czd_share")

while True:
    cmd_result = command_linux_second("tail -n 1 /opt/apache-tomcat-7.0.76/logs/catalina.out")
    if(cmd_result_last != cmd_result):
        cmd_result_last = cmd_result
        print(cmd_result)


