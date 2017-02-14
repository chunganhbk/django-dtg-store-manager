# Django DTG (Direct-to-Garment) Store Manager

A Django/Python-based app that syncs DTG vendor APIs locally to provide tools and visibility into your products to make it easier to manage.

I created this tool to allow me to make it easier to see all of my options for designing dropship printing products through Print Aura and The Printful.

*WARNING* The instructions below are outdated. Please use caution.

## Getting Started


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

*  [Docker Engine and Docker Composer](https://docs.docker.com)


### Installing


#### Step 1
Clone the repository.

#### Step 2
Build the images. This will install all the packages required using `pip` (these are listed in the [requirements.txt](./web/requirements.txt) file in case you're interested). This will probably take a little bit of time.
```
$ docker-compose build
```

#### Step 3
Now, you're ready to bring everything up. I prefer to do this when developing:

```
$ docker-compose up -d ; docker-compose logs -f
```
It brings the images up and disconnects. It then gives a live stream of the logs in a separate process so that if you break out of it (ctrl-C), it doesn't kill the machines as well. If you've not downloaded the PostgreSQL image before, it will take a little time to download it before starting everything up.

#### Step 4
In another terminal window, run the following:
```
$ docker-compose run --rm web /bin/bash
root@xxxxxxxxxxxx:/code# ./manage.py migrate
root@xxxxxxxxxxxx:/code# ./manage.py createsuperuser
root@xxxxxxxxxxxx:/code# ./manage.py shell_plus
```
This will set up the database and then create a super user (I've left this as an interactive activity so that you can set your own credentials), and then drop you into an interactive shell.

#### Step 5
If all has gone well, you should now be able to visit your site at:  ```http://localhost:8015/``` and the admin interface at ```http://localhost:8015/admin```

#### Step 6
You might notice that no products show up on the public side. You need to create a "Store" under Vendor:Printful and connect to it with your API keys.


## Built With

* [Django](https://docs.djangoproject.com/en/1.10/) - the 1.10.x series at the time of this writing.
* [Python 3.5](https://docs.python.org/3/) - the 3.5.x series at  the time of this writing.
* [Postgres](https://www.postgresql.org/docs/)


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/559labs/django-dtg-store-manager/tags).


## Authors

* **Andrew Marconi, 559 Labs** - *Initial work*, [559 Labs](https://github.com/559Labs)


## License

This open source software is licensed under the **Apache License 2.0** (see [LICENSE.md](LICENSE.md) for details).

  > A permissive license whose main conditions require preservation of copyright and license notices. Contributors provide an express grant of patent rights. Licensed works, modifications, and larger works may be distributed under different terms and without source code.


## Acknowledgments

* [WooCommerce](http://woocommerce.com/)
* [Printful](http://printful.com/)
