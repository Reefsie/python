weight = float(input('Enter your weight: '))
kg_or_lbs = str(input('kg or lbs?: '))
if kg_or_lbs == 'kg':
    print(weight * 2.20462)
elif kg_or_lbs == 'lbs':
    print(weight * 0.453592)
else:
    print('Please type only kg or lbs, and re-run the script')
