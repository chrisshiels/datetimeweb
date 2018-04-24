# datetimeweb

Sample Docker microservices with testinfra tests for Kubernetes and OpenShift.


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


## Kubernetes - Imperative

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


## OpenShift - Imperative

    host$ oc login -u developer
    host$ oc get projects
    host$ oc new-project datetimeweb \
            --description datetimeweb \
            --display-name datetimeweb
    host$ oc new-app datetimeweb/date:1.0.0
    host$ oc scale deploymentconfig date --replicas 3
    host$ oc new-app datetimeweb/time:1.0.0
    host$ oc scale deploymentconfig time --replicas 3
    host$ oc new-app datetimeweb/web:1.0.0 \
            -e DATEENDPOINT=_7001-tcp._tcp.date.datetimeweb.svc.cluster.local \
            -e TIMEENDPOINT=_7002-tcp._tcp.time.datetimeweb.svc.cluster.local
    host$ oc scale deploymentconfig web --replicas 3
    host$ oc expose service web


## OpenShift - Declarative

    host$ oc apply -f date.yaml
    host$ oc apply -f time.yaml
    host$ oc apply -f web.yaml
    host$ oc apply -f web-route.yaml
