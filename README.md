# datetimeweb

Sample Docker microservices with testinfra tests.


## Usage

    host$ # Configure virtualenv.
    host$ virtualenv virtualenv
    host$ . virtualenv/bin/activate
    (virtualenv) host$ pip install -r requirements.txt

    (virtualenv) host$ # Build images.
    (virtualenv) host$ ( cd images/date/build/ ; make VERSION=1.0.0 )
    (virtualenv) host$ ( cd images/time/build/ ; make VERSION=1.0.0 )
    (virtualenv) host$ ( cd images/web/build/ ; make VERSION=1.0.0 )

    (virtualenv) host$ # Run tests.
    (virtualenv) host$ ( cd images/date/test/ ;
                         pytest -v --image cs/date:1.0.0 )
    (virtualenv) host$ ( cd images/time/test ;
                         pytest -v --image cs/time:1.0.0 )
    (virtualenv) host$ ( cd images/web/test ;
                         pytest -v --image cs/web:1.0.0 )
