FROM fluent/fluentd:v1.16-debian-1

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ruby-dev && \
    apt-get remove -y build-essential ruby-dev && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /home/fluent/.gem/ruby/*/cache/*.gem
RUN gem install elasticsearch -v '< 8.0.0' && \
    gem install elastic-transport && \
    gem install fluent-plugin-elasticsearch -v 5.4.3


USER fluent
