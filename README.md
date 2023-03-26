### Coursework
An advertisements website with JWT authentication, separation of roles and password recovery via email.
___

### Back-end functionality:

- User authorization and authentication.
- Distribution of roles between users.
- Password recovery via Email.
- CRUD for ads on the site.
- Differentiation of access to editing/deleting ads.
- Under each ad, users can leave reviews.
- In the site header, you can search for ads by name.
___

### Tech stack:
    - Python 3.10
    - Django
    - DRF
    - Djoser
    - Postgres
    - SimpleJWT
___
### Usage:
1) Clone the repository
`git clone https://github.com/Alstacon/ToDoCon.git`.
2) Go to backend_compose.
3) Change `.env.example`'s file name for `.env` and fill it with valid parameters.
4) Run docker `docker-compose up --build -d`.
