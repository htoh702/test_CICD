FROM node:21-slim
EXPOSE 8080
COPY runapp/runapp.js .
CMD node runapp.js