# datetimeweb

Sample Docker microservices with testinfra tests for Kubernetes.


## Building and testing

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
                         pytest -v --dateimage datetimeweb/date:1.0.0 )
    (virtualenv) host$ ( cd images/time/test ;
                         pytest -v --timeimage datetimeweb/time:1.0.0 )
    (virtualenv) host$ ( cd images/web/test ;
                         pytest -v \
                             --dateimage datetimeweb/date:1.0.0 \
                             --timeimage datetimeweb/time:1.0.0 \
                             --webimage datetimeweb/web:1.0.0 )

    (virtualenv) host$ # Deactivate virtualenv.
    (virtualenv) host$ deactivate


## Kubernetes

    host$ kubectl apply -f kubernetes/date.yaml
    replicaset.apps "date" created
    service "date" created

    host$ kubectl apply -f kubernetes/time.yaml
    replicaset.apps "time" created
    service "time" created

    host$ kubectl apply -f kubernetes/web.yaml
    replicaset.apps "web" created
    service "web" created
