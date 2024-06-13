FROM nginx:alpine

# python ----------------------------------------------------------
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache bash python3 py3-pip && ln -sf python3 /usr/bin/python

# Flask/Gunicorn --------------------------------------------------
RUN pip3 install --break-system-packages --no-cache gunicorn flask flask-restful flask-cors

# Magic Wormhole for file transfers
RUN pip3 install --break-system-packages --no-cache magic-wormhole

# nginx -----------------------------------------------------------
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/
EXPOSE 80

# Supervisor (multi-process docker) -------------------------------
RUN apk add supervisor
COPY supervisord.conf /etc/supervisor/conf.d/

# App configuration
WORKDIR /app
COPY . /app

# Supervisor config runs both nginx and gunicorn/flask: -----------
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
