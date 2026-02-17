def interval_intersection(a1, b1, a2, b2):
    start = max(a1, a2)
    end = min(b1, b2)
    if start <= end:
        if start == a1 and end == b1 and start == a2 and end == b2:
            return "="
        if start == a1 and end == b1:
            return "1" 
        if start == a2 and end == b2:
            return "2"
    else:
        return None
def main():
    try:
        values = input().strip().split()
        a1, b1, a2, b2 = map(int, values)
        result = interval_intersection(a1, b1, a2, b2)
        if result:
            print(f"{result}")
        else:
            print("?")
    except ValueError:
        print()
if __name__ == "__main__":
    main()