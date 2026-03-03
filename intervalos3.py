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
        a1, b1, a2, b2 = map(int, values)
        result = interval_intersection(a1, b1, a2, b2)
        if result is None:
            print("? , []")
        else:
            if a1==a2 and b1==b2:
                print(f"= , [{result[0]},{result[1]}]")
            elif result[0] == a1 and result[1] == b1:
                print(f"1 , [{result[0]},{result[1]}]") 
            elif result[0] == a2 and result[1] == b2:
                print(f"2 , [{result[0]},{result[1]}]")
            else:
                print(f"? , [{result[0]},{result[1]}]")
    except ValueError:
        print()
if __name__ == "__main__":
    main()