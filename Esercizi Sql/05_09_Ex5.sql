/*
Create una query che visualizzi il numero di popolazione per continente
*/

select country.Continent, sum(country.Population) as Popolazione, count(country.code) as Paesi
from country
group by country.continent
order by Popolazione desc