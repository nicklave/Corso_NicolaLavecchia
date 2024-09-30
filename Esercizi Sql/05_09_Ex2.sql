/* Scrivete una query per recuperare il numero di città per nazione, 
numero ordinato in ordine decrescente */

select country.Name, count(city.ID) as COUNT
from (city
inner join country on city.CountryCode = country.code)
group by country.Name
order by COUNT desc
