from countryinfo import CountryInfo

input_country = input('Enter a country: ')
country = CountryInfo(input_country)
print('Capital is: {}'.format(country.capital()))
