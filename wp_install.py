import os
import requests

""" Download and install WORDPRESS. """

os.system("sudo wget https://wordpress.org/latest.tar.gz -P /var/www)
os.system("sudo tar zxvf /var/www/html/{}/latest.tar.gz -C /var/www)

secret_key = 'https://api.wordpress.org/secret-key/1.1/salt/'
r = requests.post(secret_key)

os.system("touch /var/www/wp-config.php")

wp_non_conf = open('Ressources/wp-config.txt', 'r')
wp_conf = open('/var/www/wp-config.php', 'w')

line = 'not_empty'

while line:
	line = wp_non_conf.readline()
	wp_conf.write(line.format(db_name=WP_DB_NAME,db_user=WP_DB_USER,db_mdp=WP_DB_PASS,key_secret=r.text))

wp_conf.close()

os.system("sudo chown -R www-data:www-data /var/www/wordpress/")
