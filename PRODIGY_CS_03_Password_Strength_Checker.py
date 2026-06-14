# Task 03 - Password Strength Checker
# Prodigy InfoTech Cyber Security Internship
# Author: Veer Nagadwala
#
# A weak password is one of the biggest security risks out there.
# This tool checks how strong your password is and tells you exactly
# what's missing so you can make it better.
#
# We check for 5 things:
#   1. Length (longer = stronger)
#   2. Uppercase letters (A-Z)
#   3. Lowercase letters (a-z)
#   4. Numbers (0-9)
#   5. Special characters (!@#$ etc.)

import re


def check_strength(password):
    score = 0
    tips = []

    # Length check - the longer the better
    if len(password) >= 12:
        score += 1
        tips.append("✅ Great length! (12+ characters)")
    elif len(password) >= 8:
        score += 0.5
        tips.append("⚠️  Decent length, but try to go for 12+ characters")
    else:
        tips.append("❌ Way too short! Use at least 8 characters (12+ is best)")

    # Does it have capital letters?
    if re.search(r"[A-Z]", password):
        score += 1
        tips.append("✅ Has uppercase letters")
    else:
        tips.append("❌ Add some uppercase letters (like A, B, C...)")

    # Does it have small letters?
    if re.search(r"[a-z]", password):
        score += 1
        tips.append("✅ Has lowercase letters")
    else:
        tips.append("❌ Add some lowercase letters (like a, b, c...)")

    # Does it have numbers?
    if re.search(r"\d", password):
        score += 1
        tips.append("✅ Has numbers")
    else:
        tips.append("❌ Add at least one number (0-9)")

    # Does it have special characters?
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\\/~`';]", password):
        score += 1
        tips.append("✅ Has special characters")
    else:
        tips.append("❌ Add special characters like !@#$%^&*")

    return score, tips


def strength_label(score):
    if score >= 4.5:
        return "💪 VERY STRONG - Excellent password!"
    elif score >= 3.5:
        return "🟢 STRONG - Good job!"
    elif score >= 2.5:
        return "🟡 MODERATE - Could be better"
    elif score >= 1.5:
        return "🟠 WEAK - Needs improvement"
    else:
        return "🔴 VERY WEAK - Please change this immediately!"


def main():
    print("\n======================================")
    print("   Password Strength Checker")
    print("   Prodigy InfoTech | Task 03")
    print("======================================")
    print("\nType a password and I'll tell you how strong it is.")
    print("Type 'quit' to exit.\n")

    while True:
        password = input("Enter password: ").strip()

        if password.lower() == "quit":
            print("\nStay safe out there! Always use strong passwords.")
            break

        if not password:
            print("You didn't enter anything. Try again!\n")
            continue

        score, tips = check_strength(password)
        label = strength_label(score)

        print(f"\n--- Results ---")
        print(f"Password length : {len(password)} characters")
        print(f"Score           : {score:.1f} / 5")
        print(f"Strength        : {label}")
        print("\nDetailed Feedback:")
        for tip in tips:
            print(f"   {tip}")
        print("-" * 40 + "\n")


if __name__ == "__main__":
    main()
