# Base image for C compilation
FROM gcc:latest

# Install Java for Java compilation
RUN apt-get update && \
    apt-get install -y default-jdk

# Create app directory
WORKDIR /app

# Keep container running
CMD ["sh"]
