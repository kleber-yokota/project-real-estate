FROM bitnami/spark:3.3.2-debian-11-r5

USER root

RUN apt update -y && apt install curl -y
RUN curl https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.2.0/delta-core_2.12-2.2.0.jar --output /opt/bitnami/spark/jars/delta-core_2.12-2.2.0.jar
RUN curl https://repo1.maven.org/maven2/io/delta/delta-storage/2.2.0/delta-storage-2.2.0.jar --output /opt/bitnami/spark/jars/delta-storage-2.2.0.jar
RUN curl https://repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.8/antlr4-runtime-4.8.jar --output /opt/bitnami/spark/jars/antlr4-runtime-4.8.jar

RUN pip install delta-spark==2.2.0 pyspark==3.3.2

USER 1001