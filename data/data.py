from dataclasses import dataclass

@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    email: str = None
    mobile: str = None
    current_address: str = None
    subject: str = None
