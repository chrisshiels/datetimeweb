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


## Kubrernetes - Imperative

    host$ kubectl run date \
            --image datetimeweb/date:1.0.0 --replicas 3 --port 7001
    host$ kubectl run time \
            --image datetimeweb/time:1.0.0 --replicas 3 --port 7002
    host$ kubectl run web \
            --image datetimeweb/web:1.0.0 --replicas 3 --port 7000 \
            --env DATEENDPOINT=date:7001 \
            --env TIMEENDPOINT=time:7002
    host$ kubectl expose deployment date --type=ClusterIP
    host$ kubectl expose deployment time --type=ClusterIP
    host$ kubectl expose deployment web --type=NodePort


## Kubernetes - Declarative

    host$ kubectl apply -f kubernetes/date.yaml
    host$ kubectl apply -f kubernetes/time.yaml
    host$ kubectl apply -f kubernetes/web.yaml
