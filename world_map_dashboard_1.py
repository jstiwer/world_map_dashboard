from countryinfo import CountryInfo
import pypopulation

input_country = input('Enter a country: ')
country = CountryInfo(input_country)
print('Capital is: {}'.format(country.capital()))
print('Alternative spelling: {}'.format(country.alt_spellings()))
print('Population is: {}'.format(pypopulation.get_population(country.alt_spellings()[0])))
