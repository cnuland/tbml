
FROM ubi8/nodejs-14:latest
RUN ls .
RUN pwd

RUN npm install @vue/cli@4.5.13 -g
RUN ls /opt/app-root/src/.npm-global/bin
ENV PATH=$PATH:/opt/app-root/src/.npm-global/bin

# Copy package.json and package-lock.json
COPY app/frontend/package*.json .

# Install app dependencies
RUN npm install --production=false

COPY app/frontend/. /opt/app-root/src

RUN npm run-script build

# Copy the dependencies into a minimal Node.js image
FROM ubi8/nginx-118:latest

# Install app dependencies

COPY --from=0 /opt/app-root/src/dist /usr/share/nginx/html

EXPOSE 8080

WORKDIR /etc/nginx

CMD ["nginx", "-g", "daemon off;"]
