Hey :)
Thanks for giving me the opportunity to do the challenge, it was fun to do it! 

## Context

After reading your email, I've asked myself two questions: 
- Which languages should I go for?
- I don't have much time, could I find some shortcuts/libs that would ease the development?

1) As I've told you during the interviews, I have a stronger experience with PHP and JavaScript so using PHP would be less challenging. Plus, not sure that a PHP implementation for a DNS Server is the most suitable approach. Considering that a part of your stack is based on Python and it's been a year that I haven't used it, it will be my choice.

2) I always like to apply KISS principle, especially when it comes about PoC. My main goal will be to get to a working solution (of course without going crappy). So any modules/libraries that could help will be considered.

I've decided that starting with the **DNS Server** would be the best considering it's a core service and the client will depend on it.

## Coding the DNS Server

After reading a few articles on how to implement it from scratch and browsing libraries I've decided to give a try to [dnslib](https://github.com/paulc/dnslib) as it supports both a DNS Server and a DNS Resolution class. The library is not the most popular but it looks like to be maintained since 2015 and got a few stars.
I've quickly got a working dns server (thanks to the doc) and moved forward with the client in order to test it. 

## Coding the Client

It's time to implement how I will commmunicate with the server.
I've used the following `{battery_id}.{payload}` url scheme that is easily splittable.
The `batteryId` will be the identifier of the battery and the `payload` will be a base64 encoded stringified json that contains the data.

## Parsing the DNS Resolution on the DNS Server

I've added a quick security to make sure I could properly split the `batteryId` from the `payload`, unless it will throw an exception.

## Failing adding RSA encryption for the payload transmission
The idea of securing the payload with a RSA ecnryption came to my mind but was quickly dropped since the encrypted output was too big.
[Each label can be up to 63 bytes long. The total length of a domain name cannot exceed 255 bytes, including the dots](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html). I think that where your idea of coding a custom protocol comes from.

## Dockerize 

Now I'm done with the main part of the challenge, it's time to think about bonuses. To be also honest, I got other ideas coming up while doing the server and the client so i'm definitely gonna need some infrastructure here.
I've then created two containers (for now), both running on python alpine linux official image.

## Adding persistence

Here we are now, I thought it would be nice to persist the data and why not to have a dashboard that displays it.
I've decided to go with Redis as it's pretty straight forward to implement. Probably a discussable choice if we want a reliable persistance but for a quick PoC it will do the job.
(We could still use AOF/RDB for more persistence)

## Consuming the persisted data

Now I have my data persisted, I need a service that is able to comsume it.
I've decided to go for a Flask API as it's very lightweight and easy to deploy.


## Building the dashboard

My choice went for a NuxtJS (with TailwindCSS) web-app with a single component that would fetch the data (using SSR) from the previously created API.
NuxtJS is definitely overkill for a single page dashboard but it was the occasion to give a try to the new Nuxt version.

## Makefile

I like to use a Makefile as it provides a simple interface to group all the cli commands.

## Mocking the data

I created a simple phony recipe inside the makefile in order to call the client and mock random data so we can have data on the dashboard.

## Testing

Interesting topic here. 
I normally like to have a TDD approach or at least unit/feature testing while coding as in my humble opinion, it gives the ability to instantly test your implementation and add coverage. Definitely something you'll thank later if times come to refactor your legacy code.
For this challenge, I haven't done it that way. Why? Because I'm not Chuck Norris :) and building a DNS Server was completely new to me. I assumed that I could probably try to implement it first and have a working server rather than spending time on how I could write my unit tests.
I ended up doing a wider communication test script that will throw an Exception if the DNS Resolution request is not succesfull. It's a simple script that is almost identical to `client.py`. So far it's not a good approach as it doesn't test the `client.py` implementation itself (wouldn't do it that way for production!). But I had issue while dealing with argv from the CI so I ended up having this shortcut.

## CI

I've added a simple github action that builds the docker compose and run the `test_connection.py` script.
I unfortunately couldn't bind the DNS Server to port 53 (used 5394 instead) as it was already binded on the github host instance.


## What I'd do with more time

- Write a protocol to handle larger payload and encrypt traffic
- Consider using [DNSStager](https://github.com/mhaskar/DNSStager) 
- Different docker compose networks to avoid exposing all containers on the same network (which is a security breach, at least for the client!)
- Split env vars to have unique env file for each service
- (Jacky tuning feature) Use redis pub/sub and socket.io to have receive new payload without refreshing the page
- Disable debug mode on the dns server / use production web server (WSGI/Gunicorn) instead of Flask/NuxtJS dev servers
- Use pylint/Flake8 for code style as pre-commit hook / CI checks
- Discuss the monorepo -> have dedicated repo for each service and more customizable CI pipelines.
- Unit tests for server / client / and api using `pyunit`
- CI on pull request and not on push (push only for demo)

## Tech Design

[![Gouach Challenge][tech-screenshot]](https://gouach.com)

[tech-screenshot]: tech-design.png



