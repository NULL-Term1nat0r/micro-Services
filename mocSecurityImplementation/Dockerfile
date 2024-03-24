# Use the official Nginx image based on Alpine Linux
FROM alpine:3.19

RUN apk update && apk add --no-cache linux-headers

# Install build dependencies
RUN apk update && apk add --no-cache \
    pcre \
    pcre-dev \
    openssl-dev \
    libxml2-dev \
    libtool \
    autoconf \
    automake \
    git \
    wget \
    gcc \
    make \
    g++ 

# Clone ModSecurity from GitHub and compile
RUN git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity /tmp/modsecurity && \
    cd /tmp/modsecurity && \
    git submodule init && \
    git submodule update && \
    ./build.sh && \
    ./configure && \
    make && \
    make install

# Copy ModSecurity configuration file
COPY modsecurity.conf /etc/nginx/modsecurity.conf
COPY index.html .

# Copy Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
