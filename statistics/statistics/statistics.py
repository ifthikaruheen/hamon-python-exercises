import argparse

def calculate_statistics(data, country, operation, from_year=None, to_year=None):
    filtered_data = [line for line in data if line[0] == country]
    
    if from_year:
        filtered_data = [line for line in filtered_data if line[2] >= from_year]
    
    if to_year:
        filtered_data = [line for line in filtered_data if line[2] <= to_year]
    
    if not filtered_data:
        return None
    
    rates = [line[3] for line in filtered_data]

    if operation == "avg":
        result = sum(rates) / len(rates)
    elif operation == "min":
        result = min(rates)
    elif operation == "max":
        result = max(rates)

    return result

def main():
    parser = argparse.ArgumentParser(description="Calculate statistics on unemployment rates")

    parser.add_argument("input_file", help="Input CSV file")
    parser.add_argument("--country", required=True, help="Country to perform operation for")
    parser.add_argument("-o", choices=["avg", "min", "max"], default="avg", help="Operation to perform on rates (default: avg)")
    parser.add_argument("--from", dest="from_year", type=int, help="Starting year (inclusive)")
    parser.add_argument("--to", type=int, help="Ending year (inclusive)")

    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as file:
            lines = [line.strip().split(",") for line in file.readlines() if line.strip()]
            
            result_in_string = calculate_statistics(lines[1:], args.country, args.o, args.from_year, args.to)
            result = float(result_in_string)
          
            if result is not None:
                print(f"Statistics for {args.country}: {args.o} Unemployment Rate = {result:.2f}")

            else:
                print(f"No data found for {args.country} in the specified range.")
    
    except FileNotFoundError:
        print(f"File '{args.input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
