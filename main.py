import os, servers, mail

ERROR = 0
bad_servers = []
There_is_a_problem = False

sender = "sender@example.com"
receivers = ("receiver@example.com")


def server_not_responding(server):

    """
    Check with a ping if the server is responding or not.
    :param server: a dictionnary containing an ip address (key = 'ip') and a hostname (key = 'hostname')
    :return: True if server is not responding, false otherwise.
    """
    try:
        state = os.system('ping -n 1 ' + servers.servers_list[index]['ip'])
        os.system('cls')
        return state != ERROR
    except Exception as e:
        print(e)

def send_email(mail_obj):
    if type(receivers) is str:
        mail_obj.send_email(sender, receivers, subject, content)
    else:
        [mail_obj.send_email(sender, receiver, subject, content) for receiver in receivers]


if __name__ == '__main__':
    for index in range(len(servers.servers_list)):
        if server_not_responding(servers.servers_list[index]):
            There_is_a_problem = True
            bad_servers.append(servers.servers_list[index])


    if There_is_a_problem:
        for index in range(len(bad_servers)):
            content = ""
            content += "CECI EST UN MESSAGE AUTOMATISÉ POUR VOUS AVISER QU'IL Y A UN PROBLÈME AVEC LES SERVEURS SUIVANTS\n\n"
            string_construct = "hostname: " + bad_servers[index]['hostname'] + " ;\t ip: " + \
                               bad_servers[index]['ip']
            content += string_construct + '\n\n\n'

        subject = "[STATUS:Problems]"

    else:
        subject = "[STATUS:Ok]"
        content = "Tous les serveurs sont up"

    send_email(mail.Mail())
