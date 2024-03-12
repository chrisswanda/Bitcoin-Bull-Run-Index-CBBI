The Colin Talks Crypto Bitcoin Bull Run Index (CBBI) is located here if you need more background - https://colintalkscrypto.com/cbbi/.

The CBBI also has an open API located here - https://colintalkscrypto.com/cbbi/data/latest.json

I wanted a way to check the daily CBBI index, automagically, along with checking to see what the trend was.  

So I built this little janky script, and I am having it run as a docker job via cron every morning at 7 am, and emails be the results.

To use, clone this repo.

Then build the image - `docker build --tag cbbi .`

edit your crontab to have - `0 7 * * * docker run --rm -v --name cbbi | mail -s "CBBI" myemail@example.com`

Then enjoy them sweet, sweet BTC returns by trying to time the market.

If you find this helpful, through a brother a bone.  

Lightning - ⚡️chrisswanda@stacker.news
BTC - bc1qev6n59q32uqja3nxsvjq8ap3f6p0jea0jeueq5

(I'll update this README for clarify and brevity later, but wanted something up here)

