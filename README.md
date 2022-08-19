> crontab -e

```
0 7 * * * /home/hitiek/docker/mintscrape/scheduled.sh -n >> /tmp/mintscrape.log 2>&1
0 19 * * * /home/hitiek/docker/mintscrape/scheduled.sh -n >> /tmp/mintscrape.log 2>&1
```
