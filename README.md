# pyTestInfra server

The goal is to get a always running test infra server that can be used to continously tests a server, and provide an external interface. 

# Requirements

To take a configuration list, run tests and provide UP/Down stats for prometheus. The idea comes from GoSS in server mode.


# Usage

I currently setup the directory structure as : https://realpython.com/python-application-layouts/#flask

but this is mostlikely no thte final way. I did do this as a flask app with prometheus, but this will not work as expected, and would rather need a loop with a web or flask endpoint. We ahsll see.

- final.py is what is the most likley iteration
- hello.py is just me getting flask running
- metrics.py is the wsgi flask example under https://prometheus.github.io/client_python/exporting/http/flask/
- prom.py is the non-flask Prometheus example under https://prometheus.github.io/client_python/getting-started/three-step-demo/

I curretly run it with:

```
flask --app dnscheck/final.py run
flask --app dnscheck/hello.py run
uwsgi --http 127.0.0.1:8000 --wsgi-file myapp.py --callable app
python3 dnscheck/prom.py 

```

It should be evident by the code on how they work. 

A few notes for myself : 

- ENUM is not what I expected ( EnumStat=State ) but rather a set of Guages with the labels for each state - and the active state has a value of 1, while the others have 0.

This also gives me more insight on how to rollout prometheus scrappers to have better stats.

