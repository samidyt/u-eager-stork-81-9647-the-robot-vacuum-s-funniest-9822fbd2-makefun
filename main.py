"""The robot vacuum's funniest excuse."""


def excuse():
    parts = [
        "I didn't miss that spot",
        "the dust bunny there pays rent",
        "and honestly it cleans up after itself.",
    ]
    return " — ".join([parts[0], parts[1]]) + ", " + parts[2]


def main():
    print(excuse())


if __name__ == "__main__":
    main()
