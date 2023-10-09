# Shield

## Docker 
```sh
docker compose up -d --build
```

## Run Migrations
```sh
docker compose exec app python3 migrations.py
```

## Documentação
A documentação de cada rota presente na aplicação basta acessar "/docs" e "/redoc"