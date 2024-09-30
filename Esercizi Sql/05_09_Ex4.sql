/*vogliamo recuperare dal database world le lingue più parlare 
per nazione con la rispettiva percentuale
*/

select country.Name, countrylanguage.Language, countrylanguage.Percentage as perc
from country
join countrylanguage on country.Code = countrylanguage.CountryCode
where countrylanguage.Percentage > 40
order by countrylanguage.Percentage desc