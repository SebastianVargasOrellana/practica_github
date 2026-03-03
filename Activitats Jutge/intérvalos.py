def interval_intersection(a1, b1, a2, b2):
    start = max(a1, a2)
    end = min(b1, b2)
    if start <= end:
        return start, end
    else:
        return None
def main():
    try:
        values = input().strip().split()
        if len(values) != 4:
            print()
            return
        a1, b1, a2, b2 = map(int, values)
        if a1 > b1 or a2 > b2:
            print()
            return
        result = interval_intersection(a1, b1, a2, b2)
        if result:
            print(f"[{result[0]},{result[1]}]")
        else:
            print("[]")
    except ValueError:
        print()
if __name__ == "__main__":
    main()