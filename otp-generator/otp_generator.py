import argparse
import secrets
import string

def generate_otp(length: int = 6) -> str:
    if not 4 <= length <= 10:
        raise ValueError("OTP length must be between 4 and 10 digits.")
    return "".join(secrets.choice(string.digits) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Generate a secure numeric OTP.")
    parser.add_argument("-l", "--length", type=int, default=6, help="OTP length (4-10)")
    args = parser.parse_args()
    try:
        print(generate_otp(args.length))
    except ValueError as error:
        parser.error(str(error))

if __name__ == "__main__":
    main()