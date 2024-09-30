select country.Name, countrylanguage.language, country.LifeExpectancy
from country
inner join countrylanguage on country.Code = countrylanguage.CountryCode
where country.GovernmentForm like '%Republic%' and countrylanguage.IsOfficial = 'T'
and country.LifeExpectancy > 70
order by country.LifeExpectancy desc