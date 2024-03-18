The Colin Talks Crypto Bitcoin Bull Run Index (CBBI) is located here if you need more background - https://colintalkscrypto.com/cbbi/.

The CBBI also has an open API located here - https://colintalkscrypto.com/cbbi/data/latest.json

I wanted a way to check the daily CBBI index, automagically, along with checking to see what the trend was.  I'm sure there are more eligant ways to do this, but I have a bare bones Raspiberry Pi that lives somewhere in my house that just does utilitarian things, such as running docker jobs or various scripts.  Now it is doing one more thing. 

So I built this little janky script, and I am having it run as a docker job via cron every morning at 7 am, and emails me the results.  At some point I'll probably integrate [Apprise](https://github.com/caronc/apprise) so that I can have multiple messaging options.  I maybe I won't.  Who knows. 

To use, clone this repo.

Then build the image - `docker build --tag cbbi .`

edit your crontab to have - `0 7 * * * docker run --rm -v --name cbbi | mail -s "CBBI" myemail@example.com`

When it runs it will output:
```
Estimated days until the Halving: 30
Trend: Down
Last 7 CBBI values: 81%, 81%, 81%, 80%, 79%, 78%, 79%
Current price of Bitcoin (in USD): $66512
```

Then enjoy them sweet, sweet BTC returns by trying to time the market.

If you find this helpful -  

Lightning - ⚡️chrisswanda@stacker.news

BTC - bc1qev6n59q32uqja3nxsvjq8ap3f6p0jea0jeueq5

(I'll update this README for clarify and brevity later, but wanted something up here)

