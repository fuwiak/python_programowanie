create user jan with encrypted password 'jan';

create database test22;

\l   ---> sprawdzanie listy dostepnych baz danych

\du+ ---> lista dostepnych uzytkownikow

grant all privileges on database test22 to jan;
