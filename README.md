# test-openshift
Just test Openshift and tox in a sample project.


# Deploying
This application supports the docker strategy

```
oc new-project test-openshift
oc new-app https://github.com/ioggstream/test-openshift --strategy=docker
oc get builds
oc get pods
```

# Adding mysql 

By default the app uses sqlite.
To use mysql either:

  - add a mysql image before adding the application
  - add a mysql image to the project and redeploy the application


