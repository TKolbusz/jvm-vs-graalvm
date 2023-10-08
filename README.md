## JVM vs GraalVM Micronaut web server comparison
Steps to follow to perform your own tests:
##JMV:
Build the project
```shell
./gradlew assemble
```
Create JVM docker image with name performance-test
```shell
docker build -t performance-test .
```
Start docker containers
```shell
docker-compose up -d
```
Perform test using Apache JMeter or other tool.

##GraalVM
Build the image
```shell
./gradlew dockerBuildNative
```
Run the image where 6ea095a128e8 is the image id from the previous command
```shell
 docker run -d --rm -p 8080:8080 6ea095a128e8
```
