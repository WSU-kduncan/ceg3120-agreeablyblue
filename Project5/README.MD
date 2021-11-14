## Lab 5 - Shawn Ruby
In this project I created resources to support a load balancing setup. To do this I modified an AWS CloudFormation Template to create 1 server accessible to the world and 2 servers accessible through SSH from the first server. Servers 2 & 3 are running Apache web server so that they can provide content that clients request from server 1. The config file that I referenced will be included in this projects repository. Please complete the following steps to setup both Apache 2 and HAProxy.

## Installing Webservers
You're going to need to install Apache webserver on both of your backend servers for this project. Follow these steps to install it on your first server and then repeat them for your second server. 

 - `sudo apt update` - Update the local package index
 - `sudo apt install apache2` - Install the apache2 package
 - `sudo ufw app list` - View the list of application profiles for your
   firewall
 - `sudo ufw allow 'Apache'` - Allow apache to send and recieve HTTP traffic
 - `sudo ufw status` - View the current status of UFW and ensure that
   Apache is allowed HTTP traffic
 - `sudo systemctl status apache2` - Check that the apache2 service is
   running
 - `curl -4 icanhazip.com` - Get your IP, after you've gotten your IP go to a web browser and enter `HTTP://yourIP`, that should take you to a site displaying this image if you've done everything correctly: 
 
![Apache default page](https://assets.digitalocean.com/articles/how-to-install-lamp-ubuntu-16/small_apache_default.png)
 
If all of the previous steps worked for you and you're seeing a page similar to the above image then you will need to update your site to use your own HTML pages. To do this you will need to do the following: 
 - `sudo mkdir /var/www/your_domain` - Create a new directory to hold your site 
 - `sudo chown -R $USER:$USER /var/www/your_domain` - Assign ownership of the directory
 - `sudo chmod -R 755 /var/www/your_domain` - Set permissions for the directory
 - `sudo nano /var/www/your_domain/index.html` - Create an index file for your new site, you can use this sample HTML code to populate the file and test out the results: 
 ````html
<html>
    <head>
        <title>Server 1 test</title>
    </head>
    <body>
        <h1>Success!  The virtual host is working!</h1>
    </body>
</html>
````

## Creating Hosts
Your proxy server is going to need easily referenced variables to access the two backend content servers. We will use Hosts to create those easily referenced variables. To create hosts you need to connect to your first server (the one that is publicly accessible and then you will need to:

 1. `sudo nano /etc/hosts` - This will allow you to edit the existing hosts file or create on if none exists
 2. `10.0.0.26 web1` - Append an entry like this to the hosts file to create a new host. *10.0.0.26* (**replace this with your servers private IP**) is the private IP of my server, and *web1* is a name that I chose to represent my server.
 3. Repeat this process for your second server, then use `ctrl + x` to exit nano editor, and type `y` confirming that you would like to save your changes to the *hosts* file

Next you will need to append a similar entry to the OpenSSL config file. To do this you will:

 1. `sudo nano /etc/ssh/ssh_config` - This will allow you to edit the existing SSH configuration file, if you've never ran SSH before you may need to create this file using `touch ssh_config`
 2. Within that file you will want to create an entry similar to this: 
  `Host web1 ` - The hostname you already created in /etc/hosts/
  `HostName 10.0.0.26` - The private IP address of the network you plan to connect to
  `User ubuntu` - The username of the account you will use when you connect to that network
  `Port 22` - The port you will use to connect to the network
  `IdentityFile ~/.ssh/ceg3120-aws-vm.pem` - The location of your private key 
  
 3. Repeat this process for your second server, then use `ctrl + x` to exit nano editor, and type `y` confirming that you would like to save your changes to the *ssh_config* file

## Installing HAProxy
With your hosts files created, and your webservers running, all that is left for this project is to install and configure HAProxy. To install HAProxy you will use the command:

 - `sudo apt install haproxy`
 
 Once that is done installing you will need to edit your config file, to do that you're going to run:
 
 - `nano /etc/haproxy/haproxy.cfg`

These are the config settings that I chose to use, you will need to update the server names to whatever you chose to name your servers: 
```
global
#global settings here
maxconn 5000
log /dev/log local0
stats socket /run/haproxy/admin.sock user haproxy group haproxy mode 660 level admin

defaults
#defaults here
timeout connect 10s
timeout client 30s
timeout server 30s
log global
mode tcp
option tcplog
maxconn 3000
  
frontend front
#frontend that accepts requests from clients
bind 10.0.0.25:80
default_backend back_end

backend back_end
#servers that fulfill the requests
balance roundrobin
server web1 10.0.0.26:80
server web2 10.0.0.27:80`
```  
 Use `ctrl + x` to exit nano editor, and type `y` confirming that you would like to save your changes to the *ssh_config* file. With that complete you need to restart HAProxy with the command `sudo systemctl haproxy` then you can run the command `sudo systemctl status haproxy` to check and make sure that your HAProxy Server is running correctly. If it is then you should be able to enter the public IP from your HAProxy server into a webbrowser and view the content from your 2 backend servers. 

   
## References

 - https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
 - https://www.haproxy.com/blog/how-to-install-haproxy-on-ubuntu/
 - http://manpages.ubuntu.com/manpages/bionic/man5/ssh_config.5.html
 - https://linuxize.com/post/using-the-ssh-config-file/
 
