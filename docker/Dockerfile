version: '3.8'

services:
  app:
    build:
      context: ..
      dockerfile: docker/Dockerfile
    ports:
      - "5000:5000"
    volumes:
      - ../:/app
    environment:
      - FLASK_ENV=development
      - HUGGINGFACEHUB_API_TOKEN=${HUGGINGFACEHUB_API_TOKEN}
    depends_on:
      - faiss_db

  faiss_db:
    image: your-faiss-db-image
    ports:
      - "8080:8080"
    volumes:
      - faiss_data:/var/lib/faiss

volumes:
  faiss_data:
