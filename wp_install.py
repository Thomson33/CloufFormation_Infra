import os
import requests
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--user", help="""DB User""")	
	
	return parser.parse_args()

""" Download and install WORDPRESS. """

ARGS = parse_arguments()

os.system("wget https://wordpress.org/latest.tar.gz -P /var/www")
os.system("tar zxvf /var/www/latest.tar.gz -C /var/www")

secret_key = 'https://api.wordpress.org/secret-key/1.1/salt/'
r = requests.post(secret_key)

os.system("touch /var/www/wordpress/wp-config.php")

wp_non_conf = open('wp-config.txt', 'r')
wp_conf = open('/var/www/wordpress/wp-config.php', 'w')

line = 'not_empty'

while line:
	line = wp_non_conf.readline()
	wp_conf.write(line.format(db_name='dsd',db_user=ARGS.user,db_mdp='zz',key_secret=r.text))

wp_conf.close()

os.system("sudo chown -R www-data:www-data /var/www/wordpress/")
