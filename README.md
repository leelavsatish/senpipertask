# senpipertask

1. Find the count of log statements in the attached(as access.log.zip) file “access.log”
with successful response (status code 200).

2. Write a command to find the files which contain words DEBUG, ERROR, and INFO
in any directory of the filesystem.

3. What would be the sed command to convert the string input "Ab1Cd2Ef3Gh4Ij5….."
to "a-bc-de-fg-hi-j…."?

4. Write a script/program to return true if the opening and closing braces are
complete, otherwise false.

    e.g:

    a. Input string:
        List { information {{about the FILEs (the current directory by default). Sort entries
        alphabetically if} none of -cftuvSUX }nor --sort } is specified.
        
        Output: True

    b. Input string:
        Performs { the specified action on the files. { Valid actions are view, cat (uses only
        "copious output" rules { and sends output to STDOUT) , compose, com‐posetyped, edit and
        print. If no action is specified, the action will be determined by how the program was called.}
        
        Output: False

5. Write steps to create and publish a docker image to the docker repository.
    e.g., Run tomcat image with a customized landing page, and should be accessible at:
    http://localhost:8080/

Bonus Question (Non Mandatory)

6. Given the following snippet of nginx server configuration:
    server {
        listen 80 default_server;
        root /var/www/html;
        server_name *.senpiper.com senpiper.com;
        }
    Write a location block for requests “/api” that will include the proxied server:
    “http://localhost:8000/welcome/home”.