- Create .env file and add the following parameters:
```
    DEBUG=False
    SECRET_KEY=...
    DATABASE_URL=postgresql://username:password@host:5432/db
    DJANGO_SETTINGS_MODULE=config.settings.production
     
    EMAIL_URL=smtp+tls://example@gmail.com:password@smtp.gmail.com:587
    REDIS_URL=redis://redis:6379
    
    POSTGRES_USER=username
    POSTGRES_PASSWORD=password
    POSTGRES_DB=db
```
-  Building production ready images & running containers:
```
    docker-compose -f docker-compose-prod.yml up --build
```