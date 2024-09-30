/*Create una vista chiamata CapitalCities che mostri 
il nome del paese e il nome della sua capitale di quel paese */

create or replace view CapitalCities as 
select country.Name as NomiPaesi, city.name as NomiCapitali
from country
inner join city on country.Capital = city.ID
