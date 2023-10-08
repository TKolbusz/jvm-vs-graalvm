# Base image
FROM openjdk:17-jdk-slim

# Set working directory
WORKDIR /app

# Copy build artifacts to container
COPY build/libs/jvm-vs-graalvm-0.1-all.jar /app/app.jar

# Expose port
EXPOSE 8080

# Start the app
CMD ["java", "-jar", "app.jar"]
