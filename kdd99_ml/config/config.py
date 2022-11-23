# !/usr/bin/python3

""" columns of the dataset """
cols ="""duration,protocol_type,service,flag,src_bytes,dst_bytes,land,wrong_fragment,urgent,hot,num_failed_logins, 
logged_in,num_compromised,root_shell,su_attempted,num_root,num_file_creations,num_shells,num_access_files,num_outbound_cmds,
is_host_login,is_guest_login,count,srv_count,serror_rate,srv_serror_rate,rerror_rate,srv_rerror_rate,same_srv_rate,diff_srv_rate,
srv_diff_host_rate,dst_host_count,dst_host_srv_count,dst_host_same_srv_rate,dst_host_diff_srv_rate,dst_host_same_src_port_rate,
dst_host_srv_diff_host_rate,dst_host_serror_rate,dst_host_srv_serror_rate,dst_host_rerror_rate,dst_host_srv_rerror_rate"""

""" The type of attacks """
attacks_types = {
    'normal': 'normal',
    'ipsweep': 'probe',
    'mscan': 'probe',
    'nmap': 'probe',
    'portsweep': 'probe',
    'saint': 'probe',
    'satan': 'probe',
    'apache2': 'dos',
    'back': 'dos',
    'land': 'dos',
    'mailbomb': 'dos',
    'neptune': 'dos',
    'pod': 'dos',
    'processtable': 'dos',
    'smurf': 'dos',
    'teardrop': 'dos',
    'udpstorm': 'dos',
    'buffer_overflow': 'u2r',
    'httptunnel': 'u2r',
    'loadmodule': 'u2r',
    'perl': 'u2r',
    'ps': 'u2r',
    'rootkit': 'u2r',
    'sqlattack': 'u2r',
    'xterm': 'u2r',
    'ftp_write': 'r2l',
    'guess_passwd': 'r2l',
    'imap': 'r2l',
    'multihop': 'r2l',
    'named': 'r2l',
    'phf': 'r2l',
    'sendmail': 'r2l',
    'snmpgetattack': 'r2l',
    'snmpguess': 'r2l',
    'spy': 'r2l',
    'warezclient': 'r2l',
    'warezmaster': 'r2l',
    'worm': 'r2l',
    'xlock': 'r2l',
    'xsnoop': 'r2l',
}

""" Protocol value mapping """
pmap = {'icmp':0,'tcp':1,'udp':2}

""" flag feature mapping """
fmap = {'SF':0,'S0':1,'REJ':2,'RSTR':3,'RSTO':4,'SH':5 ,'S1':6 ,'S2':7,'RSTOS0':8,'S3':9 ,'OTH':10}

""" attack type feature mapping """
amap = {'dos':0,'normal':1,'probe':2,'r2l':3,'u2r':4}