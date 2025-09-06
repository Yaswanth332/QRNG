# otp_detector.py
import hashlib
import random

class OTPDetector:
    def __init__(self, seed_word):
        # Same seeding logic as generator (independent)
        seed_hash = hashlib.sha256(seed_word.encode()).hexdigest()
        self.seed = int(seed_hash, 16) % (2**32)
        self.rng = random.Random(self.seed)

    def get_next_otp(self, length=6):
        """Predict the next OTP using only the seed word."""
        otp = "".join(str(self.rng.randint(0, 9)) for _ in range(length))
        return otp


if __name__ == "__main__":
    seed = "my_secret_word"

    detector = OTPDetector(seed)

    print("First OTP:", detector.get_next_otp())
    print("Second OTP:", detector.get_next_otp())
    print("Third OTP:", detector.get_next_otp())
