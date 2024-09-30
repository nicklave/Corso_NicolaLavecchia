SELECT world.city.Name, world.country.Name, world.countrylanguage.Language  
FROM ((world.city
inner join country on world.city.CountryCode = world.country.Code )
inner join countrylanguage on world.countrylanguage.CountryCode = world.country.Code);
