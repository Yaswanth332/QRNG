# otp_generator.py
import hashlib
import random

class OTPGenerator:
    def __init__(self, seed_word):
        # Convert seed word to numeric seed
        seed_hash = hashlib.sha256(seed_word.encode()).hexdigest()
        self.seed = int(Aseed_hash, 16) % (2**32)
        self.rng = random.Random(self.seed)

    def generate_otp(self, length=6):
        """Generate a numeric OTP of given length."""
        otp = "".join(str(self.rng.randint(0, 9)) for _ in range(length))
        return otp


if __name__ == "__main__":
    gen = OTPGenerator("my_secret_word")
    print("First OTP:", gen.generate_otp())
    print("Second OTP:", gen.generate_otp())
    print("Third OTP:", gen.generate_otp())
