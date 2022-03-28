# class modelo de cliente

class Client:
    def __init__(self, nome: str, email: str):
        self._nome = nome
        self._email = email

    def __str__(self) -> str:
        return f'''Nome:{self._nome}\nEmail:{self._email}'''

    @property
    def nome(self, ) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email
