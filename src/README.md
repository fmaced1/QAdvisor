# docker login

# Sonar
# docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube

# Redis
# docker network create redis
# docker run -d --name=redis --network redis -p 6379:6379 redis:latest

# Build image
# docker build -t fin-advisor:1.0.0 .

# Creating network
# docker network create redis

# Run Dashboard container
# docker run -d --network=redis -v $(pwd)/src:/src -p 8501:8501 --name=fin-advisor fin-advisor:1.0.0

# Streamlit
# Acess -> 0.0.0.0:8501