import re

async def sanitize_user_data(user_data):
  email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
  password_regex = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{6,}$"

  for key, value in user_data.items():
    if isinstance(value, str):
      value = value.strip()
      
    if key in {"fname", "lname", "username"}:
      user_data[key] = value.lower()

    elif key == "email":
      if not re.match(email_regex, value):
        raise ValueError("Invalid email format")
      user_data[key] = value.lower()

    elif key == "password":
      if not re.match(password_regex, value):
        raise ValueError("Password must be at least 6 characters, including one letter and one number")
      user_data[key] = value

  return user_data 


