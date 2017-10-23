import actions
def RunCommandOnAnsible(command):
    ansible_primary_server='10.142.128.102'
    ansible_user='letv'
    ansible_password='SCM@le.com'
    server=actions.Server(host=ansible_primary_server, port=22, username=ansible_user, password=ansible_password)    
    result=server.execute(command)
    return result    


def send_email(subject,content,receiver):
    sender="SEE@le.com"
    command='cd /letv/scripts/report/;python mail.py \"%s\" \"%s\" \"%s\" \"%s\"' %(subject,content,sender,receiver)
    print command
    RunCommandOnAnsible(command)
        
subject="VM random password of 10.142.128.97"
content="the random password of VNC,samba,system account is 'nfeu6', you can run command 'vmcfg' to modify the password unified"
receiver="yangaofeng@le.com"
send_email(subject,content,receiver)
