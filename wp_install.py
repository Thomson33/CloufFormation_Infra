import os
import requests
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--user", help="""DB User""")
	parser.add_argument("-l", "--host", help="""DB Host""")
	parser.add_argument("-p", "--password", help="""DB Pass""")
	parser.add_argument("-n", "--name", help="""DB Name""")
	parser.add_argument("-a", "--access", help="""S3 Access Key""")
	parser.add_argument("-s", "--secret", help="""S3 Secret Key""")
	return parser.parse_args()

""" Download and install WORDPRESS. """

ARGS = parse_arguments()

#os.system("wget https://wordpress.org/latest.tar.gz -P /var/www")
#os.system("tar zxvf /var/www/latest.tar.gz -C /var/www")

secret_key = 'https://api.wordpress.org/secret-key/1.1/salt/'
r = requests.post(secret_key)

os.system("touch /var/www/wp-config.php")

wp_non_conf = open('wp-config.txt', 'r')
wp_conf = open('/var/www/wp-config.php', 'w')

line = 'not_empty'

while line:
	line = wp_non_conf.readline()
	wp_conf.write(line.format(db_host=ARGS.host, db_name=ARGS.name, db_user=ARGS.user, db_mdp=ARGS.password, s3_access=ARGS.access, s3_secret=ARGS.secret, key_secret=r.text))

wp_conf.close()

os.system("sudo chown -R www-data:www-data /var/www/")
