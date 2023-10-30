FROM openjdk:17.0.2-jdk
VOLUME /tmp

# PORT and ENVIRONMENT VARIABLES
# Recommended port
#EXPOSE 8080
ENV PORT value

# Bucket info
ENV ACCESS_KEY value
ENV SECRET_ACCESS_KEY value
ENV REGION value

# Database info
ENV DATABASE_URL value
ENV DATABASE_USERNAME value
ENV DATABASE_PASSWORD value

ADD target/spring-boot-API.jar spring-boot-API.jar
ENTRYPOINT ["java","-jar","/spring-boot-API.jar"]