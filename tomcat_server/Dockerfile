# Use the official Tomcat image as the base
FROM tomcat:9.0

# Copy custom landing page into the webapps directory of Tomcat
COPY webapp/index.html /usr/local/tomcat/webapps/ROOT/index.html

# Expose port 8080
EXPOSE 8080

# Start Tomcat when the container runs
CMD ["catalina.sh", "run"]