FROM node:19-alpine3.15
RUN apk --no-cache add nodejs yarn --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community
WORKDIR /web-app
COPY ./src .
RUN yarn install
EXPOSE 3001
ENV PORT=3001
CMD ["yarn", "dev"]