Title: My Adventure in Building Umami
Date: 2024-04-05 7:37pm
Category: Misc
Tags: misc
Slug: analytics
Summary: How I set up website analytics tracking with Umami
status: hidden

<script src="{attach}/scripts/medium-zoom.js"></script>

<script src="{attach}/scripts/nutshelldev.js"></script>
<script>
Nutshell.setOptions({
    dontEmbedHeadings: true, // If 'true', removes the "embed this as a nutshell" option on headings
});
</script>


I'll be testing [Nutshell](https://github.com/ncase/nutshell){: target="_blank"} out! When you see a link like [:this](#note1), click on it to expand it.

---

![umami screens overlaid]({attach}/images/umami/cover.jpg){: .zoomable}


[Umami](https://umami.is/){: target="_blank"}. is an open source analytics provider focused on privacy. This means you can see information about people who visit your website, like their country. 

You can find Starly's analytics dashboard [here](https://umami.starly.dev/share/hNfhWdonj5bA5dBj/starly.dev){: target="_blank"} !

---

Google Analytics has more metrics, but I didn't need a lot of their advanced features (who would have thought my tiny blog wouldn't need ad revenue tracking). And lack of privacy and GDPR non-compliant or something. 

There's other Google Analytics alternatives, but they cost money, so I didn't read much of their websites. 

If you're just here to figure out installing Umami without any extra bits, you'll be fine following only the bullet points. 

---

## Software Requirements
- i am using Ubuntu 23.10 on a Digital Ocean instance
- install Node.js, [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04){: target="_blank"}
- install PostgreSQL, [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-22-04){: target="_blank"}
    - you can also use MySQL with Umami, but this post uses postgres

actual install docs from umami are [here](https://umami.is/docs/install){: target="_blank"}

## Install and run Umami


1. **set up yarn**
    - run `corepack enable`
    
    We use Yarn (package manager, similar to npm) to install necessary packages. This is activated with corepack, which comes with our Node.js installation. 
    
    You can use npm instead, but I haven't tried it. 
    
    For more info, yarn installation docs are [here](https://yarnpkg.com/getting-started/install){: target="_blank"}

2. **set up umami**
    - `git clone https://github.com/umami-software/umami.git`
    - `cd umami`
    - `yarn`

    To set up Umami, clone the repo and run `yarn` inside, which looks at the `package.json` file in the repo and downloads the packages specified there. 

3. **set up postgres and connection string**
    - run `createdb --username=postgres --host=localhost umami`
    - create a `.env` file in the cloned umami folder
    - put this line in `.env`, filling in your Postgres's details: `DATABASE_URL=postgresql://[USERNAME]:[PASSWORD]@[DB_LOCATION]:[PORT]/[DATABASE_NAME]`
        - if this string is incorrect, it will show this [:error](#error)
    
    Use the `createdb` command to create a database called umami. Then, put your connection string into a new `.env` file so Umami knows how to connect to your Postgres instance and which database to put the metrics in. 

    my [:example string](#postgresNote1).
    
    Note: If you've installed postgres for the first time, you may want to make another user besides the default (postgres), set a password, or change authentication methods.

1. **build Umami**
    - `yarn build`
    - some optional things:
        - `yarn next telemetry disable` to disable Next.js telemetry
        - to change the port next.js uses (default is 3000), go to `package.json`, change `next start` to be `next start -p [new port]`

    Running `yarn build` looks at the `scripts` section of `package.json` and executes the commands found under `build`.
    
    Note: Building eats a lot of memory and the base Digital Ocean server may not have enough memory to run it without upgrading or configuring more swap (I learned the hard way!). 
    
    [:More about swap](#swap)

2. **start Umami**
    - run `npm start`
    - go to `http://[IP]:3000/`, where `[IP]` is the IP address of your server
    - log in
        - username: admin
        - password: umami
        - log in [:screenshot](#login)
    - go to Settings -> Users to change your password

    Optional: use [PM2](https://pm2.keymetrics.io/docs/usage/quick-start/){: target="_blank"}, a process manager, to manage your Umami instance. This makes it easier to start and stop Umami when it stops running, like when you restart your server. 

    - `npm install pm2 -g`
    - `pm2 start npm --name umami -- start`
        - make sure you're in the umami folder before running
    - `pm2 save`

    These steps install PM2 globally, start the Umami instance with PM2, and saves the process in a list that you can easily restart later (with `pm2 start all` and `pm2 stop all`)

3. **set up site**
    - in Umami, go to Settings > Websites
    - click Add Website
        - name: can be anything you want (e.g. starly)
        - domain: your website domain (e.g. starly.dev)
        - add website [:screenshot](#add_site)
    - click edit > tracking code 
        - copy tracking code and put it in the `<head>...</head>` tag of each website page you want to track
        - tracking code [:screenshot](#screenshot)
    - optional:
        - edit > enable share URL if you'd like to share the dashboard
    - test by going to your website and seeing if the visitor count goes up

    If you don't want to track your own visits to your website, you can add `umami.disabled` with a value of `1`.

    [:How?](#disable)

---

There's other things to play around with like reports and insights, but I haven't gotten around to it yet. 

At this point, you're done setting Umami up and have reliable metrics about your website! 

## There's *more*??

One other thing I did was set up `umami.starly.dev` as the domain to send (proxy) Umami requests to using Nginx. This means that you can access Umami at your chosen domain instead of `http://[IP]:3000/`.

If your website is hosted on the same server that you're running Umami on, you only need to add an Nginx configuration to change the domain. However, because I'm running most of the website on Github Pages, I also had to change my DNS settings to tell the internet where `umami.starly.dev` is. 

If you want to use https, you will have to set up SSL certs on your server. 

Nginx install [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04){: target="_blank"}.

## Proxy Umami Requests

1. **set up DNS so requests go to your server** <br> (only needed if Umami and your website are hosted in different places!!!!!)
    - add a new A record to your DNS 
        - name: the subdomain you want to use
            - e.g. use umami if you want to point to `umami.starly.dev`
        - address: your server's IP address
    - [:What should my DNS look like?](#dns)

2. **set up nginx config so requests go to Umami**
    - run `systemctl status nginx` to check if nginx is running
        - if not, try `sudo systemctl start nginx`
    - go to `/etc/nginx/nginx.conf` and remove any `location /` blocks currently inside
    - paste the following inside the `http { }` block

            :::nginx
            server {
                listen 80;
                listen [::]:80;

                server_name umami.yourdomain.com;

                location / {
                    proxy_pass http://localhost:3000;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header Host $host;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                }
            } 

    - example of [:`nginx.conf`](#nginx)
    - run `sudo nginx -s reload` to reload config changes
    - go to `umami.yourdomain.com` and check if it pulls up the Umami website

     The config tells nginx to listen on port 80 (which is where internet traffic goes through). Now, when someone goes to `http://umami.yourdomain.com`, nginx hears it and knows to return whatever is at `localhost:3000` to that person.

    If you can't access it, here are some [:troubleshooting steps](#troubleshoot)

            
3. **set up SSL certs** <br> (only needed if you want https support!!!!!!)

    [:What's http/https? Why would I need an SSL cert?](#https)

    There are two different ways to get an SSL certificate: 

    - Let's Encrypt
    - Cloudflare
        - If you're already using Cloudflare to manage DNS, it's easier to use Cloudflare

    I have not used Let's Encrypt, so this guide only covers Cloudflare. Here are Let's Encrypt's directions:

    - [Getting Started](https://letsencrypt.org/getting-started/){: target="_blank"}
    - [Instructions](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal){: target="_blank"} for nginx and Ubuntu

    Steps for using Cloudflare certs:

    1. **generate TLS cert**
        - login to Cloudflare, go to the TLS/SSL section (found on the left), then Origin Server
        - click Create Certificate and don't change the options 
        - click Create to see your new certificate's information
            - Note: **do not** leave the information page without copying your private key
        - copy the Origin Certificate into `/etc/ssl/cert.pem` on your server
        - copy your private key into `/etc/ssl/key.pem` on your server 
            - Note: make sure your certs don't have spaces or newlines

    2. **update nginx config**
        - paste the following under your previous server block listening on port 80

                :::nginx
                server {
                    listen 443 ssl http2;
                    listen [::]:443 ssl http2;
                    ssl_certificate         /etc/ssl/cert.pem;
                    ssl_certificate_key     /etc/ssl/key.pem;

                    server_name umami.starly.dev;

                    location / {
                        proxy_pass http://localhost:3000/;
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_set_header Host $host;
                        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    }
                }

        - example of [:nginx.conf](#nginx2)
        - Now, you should be able to access Umami from `https://umami.starly.dev`. 

    You can also change your tracking code to use `umami.yourdomain.com` (you can copy the code again from Umami)

## Updating

It's simple to update your Umami instance when a new version comes out! 

- `cd umami`
- `git pull`
- `yarn`
- `yarn build`
- `npm start` or `pm2 reload umami` for PM2

These steps fetch the update from Github, install any new dependencies from the update, rebuild Umami, and restart it. 

## How does Umami work?

How does Umami get data from visitors and put it into your dashboard? 

When you put your Umami tracking code into the `<head>` tag of your website, the [`script.js`](https://github.com/umami-software/umami/blob/88da20ea7f9e34a3d09cf8503ae09bff63b254bc/src/tracker/index.js){: target="_blank"} file on your server gets called. The script gets information from http headers like which website page you're looking at and listens for any events that you've set up with Umami (such as button clicks). 

Next, this information is sent to your database, and when you look at the dashboard, it pulls that information for you. 

If you're using nginx, you may have noticed the following lines:

    :::nginx
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

These headers are forwarded from the original request to Umami, so even if you're proxying the connection, Umami can still get the data it needs for analytics. 

## Summary

Overall, Umami is a great tool to get analytics about your website. Just install Umami from the Github repository onto your server and put your tracking code onto your website. If desired, you can set up a subdomain for Umami using Nginx. 

## :x note1
hi!

## :x postgresNote1
`DATABASE_URL=postgresql://username:password@localhost:5432/umami`

- Postgres's default port is 5432, so use this if you have not configured another port 
- Use localhost if your Postgres is on the same server as Umami; otherwise, use the IP of the server Postgres is located on

## :x error

    ✓ DATABASE_URL is defined.
    ✗ Unable to connect to the database.
    error Command failed with exit code 1.

## :x swap

Swap is hard drive space used as RAM. Although it is much slower than actual RAM, it can be used when you run out of actual RAM. However, it will slow your system down a lot. 

The following commands let you configure swap on your server, where count is the amount of memory you'd like to use for swapping. 

```bash
sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
sudo /sbin/mkswap /var/swap.1
sudo /sbin/swapon /var/swap.1
```

- First command makes a file in `/var` named `swap.1` with 1024mb filled with 0s (basically just allocating space for the file).
- Second command formats the swap.1 file as a swap area. 
- Third command tells the OS you'd like to start using the swap space

This change will not be permanent unless you add this info to your `/etc/fstab` file, which is where your OS references information about how to open file systems like USBs or where swap is. 

Another parameter that can be configured is swappiness, which controls how often swap is used. It goes from 0-100: 0 means swap will not be used until the system runs out of RAM, and 100 means swap will start being used almost immediately. The default is 60, meaning swap will be used at around 60% of RAM usage. 

This value can be checked with `cat /proc/sys/vm/swappiness`

More info [here](https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-22-04)

Windows has a similar concept called page / pagefile; [here](https://stackoverflow.com/a/1689119) is a good summary of both.

## :x login 
![screenshot of umami's login page]({attach}/images/umami/login.png)

## :X add_site
![screenshot of adding a website in umami]({attach}/images/umami/add_site.png)

## :x screenshot

![screenshot of where to find tracking code]({attach}/images/umami/script.png)

## :x disable

1. go to your website and inspect element
2. go to the Application tab 
3. go to Cookies
4. double click the next available space below `Name` and type `umami.disabled`
5. add a value to it of `1`

![cookie example]({attach}/images/umami/cookie.png)


## :x dns
![screenshot of DNS settings]({attach}/images/umami/dns.png)

Note: I have the Github A records because I use Github Pages to host my website

## :x nginx

    :::nginx
    user www-data;
    worker_processes auto;
    pid /run/nginx.pid;
    error_log /var/log/nginx/error.log;

    events {
            worker_connections 768;
    }

    http {
            sendfile on;
            tcp_nopush on;
            types_hash_max_size 2048;
            include /etc/nginx/mime.types;
            default_type application/octet-stream;
            ssl_prefer_server_ciphers on;

            access_log /var/log/nginx/access.log;
            gzip on;

            server {
                listen 80;
                listen [::]:80;

                server_name umami.starly.dev;

                location / {
                    proxy_pass http://localhost:3500/;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header Host $host;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                }
            }
    }

## :x troubleshoot
- run `sudo nginx -t` to check for syntax errors (should say OK)
- check `/var/log/nginx/error.log` to look at logged errors
- run `systemctl status nginx` to ensure nginx is running
- run `sudo ufw status` to check if your firewall is allowing connections in/out

## :x https
http is a way for computers to fetch the website data you've requested. https is the same protocol, but there's an extra layer of security on top. 

When you go to a website with https, your browser checks the website's SSL certificate. Your browser does a TLS handshake, which is an exchange of encryption keys between you and the website's server made possible by the SSL certificate's information. 

Now, your browser can encrypt your data using these keys so that only you and the website can read your data. The certificate also ensures the website you're going to is who they claim to be.

## :x nginx2

    :::nginx
    user www-data;
    worker_processes auto;
    pid /run/nginx.pid;
    error_log /var/log/nginx/error.log;

    events {
            worker_connections 768;
    }

    http {
            sendfile on;
            tcp_nopush on;
            types_hash_max_size 2048;
            include /etc/nginx/mime.types;
            default_type application/octet-stream;
            ssl_prefer_server_ciphers on;

            access_log /var/log/nginx/access.log;
            gzip on;

            server {
                listen 80;
                listen [::]:80;

                server_name umami.starly.dev;

                location / {
                    proxy_pass http://localhost:3500/;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header Host $host;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                }
            }

            server {
                listen 443 ssl http2;
                listen [::]:443 ssl http2;
                ssl_certificate         /etc/ssl/cert.pem;
                ssl_certificate_key     /etc/ssl/key.pem;

                server_name umami.starly.dev;

                location / {
                    proxy_pass http://localhost:3000/;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header Host $host;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                }
            }
    }

<script>  
const zoom = mediumZoom('.zoomable')
</script>