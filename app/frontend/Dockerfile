
FROM ubi8/nodejs-14:latest
RUN ls .
RUN pwd

# Copy package.json and package-lock.json
COPY app/frontend/package*.json .

# Install app dependencies
RUN npm install --production

# Copy the dependencies into a minimal Node.js image
FROM registry.access.redhat.com/ubi8/nodejs-14-minimal:latest

# Install app dependencies
USER 0
RUN ls /opt/app-root/src
COPY --from=0 /opt/app-root/src/node_modules /opt/app-root/src/node_modules
COPY app/frontend/. /opt/app-root/src
RUN ls .
RUN pwd
RUN npm install @vue/cli@4.5.13

ENV NODE_ENV production
ENV PORT 3000
EXPOSE 3000
CMD ["npm", "run", "serve"]
