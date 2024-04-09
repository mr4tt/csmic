Title: My Adventure in Building Umami
Date: 2024-04-05 7:37pm
Category: Misc
Tags: misc
Slug: analytics
Summary: How I set up website analytics tracking with Umami
status: hidden

<script src="{attach}medium-zoom.js"></script>

<script src="{attach}nutshelldev.js"></script>
<script>
Nutshell.setOptions({
    dontEmbedHeadings: true, // If 'true', removes the "embed this as a nutshell" option on headings
});
</script>


I'll be testing [Nutshell](https://github.com/ncase/nutshell) out! When you see a link like [:this](#note1), click on it to expand it.

---



![umami screens overlaid]({attach}/images/umami/cover.jpg){: .zoomable}


[Umami](https://umami.is/). is an open source analytics provider focused on privacy. This means you can see information about people who visit your website, like their country. 

You can find Starly's analytics dashboard [here](https://umami.starly.dev/share/hNfhWdonj5bA5dBj/starly.dev) !

---

Google Analytics does similar things, but I didn't need a lot of their advanced features (who would have thought my tiny blog wouldn't need ad revenue tracking). And lack of privacy and GDPR non-compliant or something. 

There's other Google Analytics alternatives, but they cost money, so I didn't read much of their websites. 

If you're just here to figure out installing Umami without any extra bits, you'll be fine following only the bullet points. 

---

## Software Requirements
- i am using Ubuntu 23.10 on a Digital Ocean instance
- install Node.js, [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04){: .blue-link}
- install Nginx, [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04){: .blue-link}
- install PostgreSQL, [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-22-04){: .blue-link}
    - you can also use MySQL with Umami, but this post uses postgres

actual install docs from umami are [here](https://umami.is/docs/install)

## Install and run Umami


1. **set up yarn**
    - run `corepack enable`
    
    We use Yarn (package manager, similar to npm) to install necessary packages. This is activated with corepack, which comes with our Node.js installation. 
    
    You can use npm instead, but I haven't tried it. 
    
    For more info, yarn installation docs are [here](https://yarnpkg.com/getting-started/install)

2. **set up umami**
    - `git clone https://github.com/umami-software/umami.git`
    - `cd umami`
    - `yarn`

    To set up Umami, clone the repo and run `yarn` inside, which looks at the `package.json` file in the repo and downloads the packages specified there. 

3. **set up postgres and connection string**
    - run `createdb --username=postgres --host=localhost umami`
    - create a `.env` file in the cloned umami folder
    - put this line in `.env`, filling in your Postgres's details: `DATABASE_URL=postgresql://[USERNAME]:[PASSWORD]@[DB_LOCATION]:[PORT]/[DATABASE_NAME]`
    
    Use the `createdb` command to create a databse called umami. Then, put your connection string into a new `.env` file so Umami knows how to connect to your Postgres instance and which database to put the metrics in. 

    my [:example string](#postgresNote1).
    
    Note: If you've installed postgres for the first time, you may want to make another user besides the default (postgres), set a password, or change authentication methods.

4. **build Umami**
    - `yarn build`
    - some optional things:
        - `yarn next telemetry disable` to disable Next.js telemetry
        - to change the port next.js uses (default is 3000), go to `package.json`, change `next start` to be `next start -p [new port]`

    Running `yarn build` looks at the `scripts` section of `package.json` and executes the commands found under `build`.
    
    Note: Building eats a lot of memory and the base Digital Ocean server may not have enough memory to run it without upgrading or configuring more swap (I learned the hard way!). 
    
    [:More about swap](#swap)

5. **start Umami**
    - run `npm start`
    - go to `http://[IP]:3000/`
    - log in:
        - username: admin
        - password: umami
    - go to settings to change your password

    Optional: use [PM2](https://pm2.keymetrics.io/docs/usage/quick-start/), a process manager, to manage your Umami instance. This makes it easier to start and stop Umami when it stops running, like when you restart your server. 

    - `npm install pm2 -g`
    - `pm2 start npm --name umami -- start`
        - make sure you're in the umami folder before running
    - `pm2 save`

    These steps install PM2 globally, start the Umami instance, and saves it in a list that you can easily restart later.

6. **set up site**
    - in Umami, go to Settings > Websites
    - click Add Website
        - name: can be anything you want (eg: starly)
        - domain: your website domain (eg: starly.dev)
    - click edit > tracking code 
        - copy tracking code and put it somewhere in the `<head>...</head>` tag of your website
        - [:screenshot](#screenshot)
    - optional:
        - edit > enable share URL if you'd like to share the dashboard
    - test by going to your website and seeing if the visitor count goes up

    If you don't want to track your own visits to your website, you can add `umami.disabled` with a value of `1`.

    [:How?](#disable)

---

There's other things to play around with like reports and insights, but I haven't gotten around to it yet. 

At this point, you're done setting Umami up and have reliable metrics about your website! 

## There's *more*??

One other thing I did was set up umami.starly.dev as the domain to send (proxy) Umami requests to. This means that you can access Umami at your chosen domain instead of `http://[IP]:3000/`.

If your website is hosted on the same server that you're running Umami on, you only need to add an Nginx configuration to change the domain. However, because I'm running most of the website on Github Pages, I also had to change my DNS settings to tell the internet where umami.starly.dev is. 

If you want to use https, you will have to set up SSL certs on your server. 

## Proxy Umami Requests

1. **set up DNS so requests go to your server** <br> (only needed if Umami and your website are hosted in different places!!!!!)
    - add a new A record to your DNS 
        - name: the subdomain you want to use
            - eg: use umami if you want to point to umami.starly.dev
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

    The config does x and y 

    - If you can't access it, here are some troubleshooting steps:
        - run `sudo nginx -t` to check for syntax errors (should say OK)
        - check `/var/log/nginx/error.log` to look at logged errors
        - ensure nginx is running
        - run `sudo ufw status` to check if your firewall is on or not allowing connections in 


            
3. **set up SSL certs**
    - i dont remember lol

u can now change your tracking code 

## Updating

It's simple to update your Umami instance when a new version comes out! 

- `cd umami`
- `git pull`
- `yarn`
- `yarn build`
- `npm start` or `pm2 reload umami` for PM2

These steps fetch the update from Github, install any new dependencies from the update, rebuild Umami, and restart it. 

## How does Umami work?

`<script defer="" src="https://umami.starly.dev/script.js" data-website-id="really-cool-string"></script>`

This calls [`script.js`](https://github.com/umami-software/umami/blob/88da20ea7f9e34a3d09cf8503ae09bff63b254bc/src/tracker/index.js), which in turn does some stuff i guess idk 

test
<kbd> hi </kbd>

## :x note1
hi!

## :x postgresNote1
`DATABASE_URL=postgresql://username:password@localhost:5432/umami`

- Postgres's default port is 5432, so use this if you have not configured another port 
- Use localhost if your Postgres is on the same server as Umami; otherwise, use the IP of the server Postgres is located on

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

<script>  
const zoom = mediumZoom('.zoomable')
</script>