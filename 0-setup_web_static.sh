#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Update and upgrade system packages
sudo apt-get -y update
sudo apt-get -y upgrade

# Install Nginx
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a test HTML file
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the test release
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership to the ubuntu user
sudo chown -hR ubuntu:ubuntu /data/

# Configure Nginx to serve static content
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart
