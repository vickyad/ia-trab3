import eight_queens as eq

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = eq.run_ga_with_data_generation(200, 100, 20, 0.6, True)
    print(f'{result} - {eq.evaluate(result)} conflitos')
